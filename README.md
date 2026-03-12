# 📊 StatViz-Statistical-Analysis-Visualization

A simple web application built with Flask that performs statistical analysis on a set of numbers and visualizes the data with interactive charts. Users can enter comma‑separated numbers, view key statistics (mean, median, range, outliers), and generate bar, line, or pie charts. The results and the selected chart can be downloaded as a PDF report.

---

## ✨ Features

- **Statistical summary** – mean, median, range, and outliers (based on the interquartile range method).
- **Interactive charts** – choose between bar, line, or pie charts (powered by Chart.js).
- **PDF report** – download a report containing the original data and the generated graph (uses Matplotlib and ReportLab).
- **Clean, responsive interface** – works on desktop and mobile.

---

## 🛠 Technologies

- **Backend**: Python, Flask
- **Data processing**: statistics (standard library), NumPy
- **Charts**: Matplotlib (for PDF), Chart.js (for interactive display)
- **PDF generation**: ReportLab
- **Frontend**: HTML, CSS, JavaScript

---

## 📂 Project Structure

```
StatViz-Statistical-Analysis-Visualization/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/statistical-analysis-tool.git
cd statistical-analysis-tool
```

### 2. Create a virtual environment (recommended)

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

**Linux / Mac**

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install flask numpy matplotlib reportlab
```

---

## ▶️ Run the Application

Start the Flask server:

```
python app.py
```

Then open your browser and visit:

```
http://localhost:10000
```

---

## 🧑‍💻 How to Use

1. Enter numbers separated by commas.

Example:

```
10, 20, 30, 40, 50
```

2. Click **Analyze** to calculate statistics.

3. View the results (mean, median, range, outliers).

4. Select a **chart type**:

   * Bar
   * Line
   * Pie

5. Click **Show Graph** to display the chart.

6. Click **Download PDF** to save the report.

---

## 📦 Example Input

```
5, 10, 15, 20, 25, 30
```

Output includes:

* Statistical summary
* Data visualization
* Downloadable PDF report

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙌 Contributing

Contributions are welcome!
You can improve this project by:

* Adding more statistical functions
* Improving the user interface
* Adding CSV / Excel export
* Enhancing charts and reports

---

⭐ If you find this project useful, consider giving it a **star** on GitHub!


## 📁 Project Structure
