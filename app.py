from flask import Flask, render_template, request, send_file
import statistics
import numpy as np
import matplotlib
matplotlib.use("Agg")               # Use non-interactive backend for server
import matplotlib.pyplot as plt
import io
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

# Global variables to remember the last submitted data and graph type for PDF export
last_data = []
last_graph = "bar"

@app.route("/", methods=["GET", "POST"])
def index():
    global last_data
    result = None
    data = []

    if request.method == "POST":
        # Get numbers from form (comma separated)
        numbers = request.form["numbers"]
        # Convert to list of floats
        data = [float(x.strip()) for x in numbers.split(",")]
        last_data = data                     # Save for PDF download

        # Basic statistics
        result = {
            "sum": round(sum(data), 2),
            "mean": round(statistics.mean(data), 2),
            "median": statistics.median(data),
            "min": min(data),
            "max": max(data),
            "range": max(data) - min(data),
            "q1": np.percentile(data, 25),
            "q2": np.percentile(data, 50),
            "q3": np.percentile(data, 75)
        }

        # Interquartile range and outliers (Tukey's fences)
        result["iqr"] = result["q3"] - result["q1"]
        lower_fence = result["q1"] - 1.5 * result["iqr"]
        upper_fence = result["q3"] + 1.5 * result["iqr"]
        outliers = [x for x in data if x < lower_fence or x > upper_fence]
        result["outliers"] = outliers if outliers else "None"

    # Render template with results and the original data (for chart)
    return render_template("index.html", result=result, data=data)


@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    global last_data, last_graph
    graph_type = request.form["graphType"]      # 'bar', 'line', or 'pie'
    last_graph = graph_type
    data = last_data

    # Frequency of each value
    freq = {}
    for val in data:
        freq[val] = freq.get(val, 0) + 1
    labels = list(freq.keys())
    values = list(freq.values())

    # Create a matplotlib figure
    img_bytes = io.BytesIO()
    plt.figure()

    if graph_type == "bar":
        plt.bar(labels, values)
    elif graph_type == "line":
        plt.plot(labels, values, marker='o')
    elif graph_type == "pie":
        plt.pie(values, labels=labels, autopct="%1.1f%%")

    plt.title("Data Distribution")
    plt.savefig(img_bytes, format='png')
    plt.close()
    img_bytes.seek(0)

    # Create PDF with ReportLab
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer)
    c.drawString(200, 800, "Statistical Analysis Report")
    c.drawString(50, 760, f"Data: {data}")

    # Save matplotlib image temporarily and embed in PDF
    with open("temp_graph.png", "wb") as f:
        f.write(img_bytes.getbuffer())
    c.drawImage("temp_graph.png", 100, 400, width=400, height=300)

    c.save()
    pdf_buffer.seek(0)

    # Clean up temporary file (optional)
    if os.path.exists("temp_graph.png"):
        os.remove("temp_graph.png")

    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name="report.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)