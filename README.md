# 🛒 Retail AI Dataset Preparation Pipeline

A production-style Python pipeline for validating, cleaning, and preparing retail product datasets for AI model training.

---

## 📖 Overview

This project demonstrates how raw retail product datasets can be transformed into clean, validated datasets suitable for machine learning and computer vision applications.

The pipeline automates common data quality checks and preprocessing tasks required before AI model training.

---

## ✨ Features

- ✅ Dataset validation
- ✅ Duplicate row removal
- ✅ Empty row removal
- ✅ Text normalization
- ✅ Coordinate validation
- ✅ Price validation
- ✅ Automatic quality report generation
- ✅ Clean dataset export

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Git
- GitHub

---

## 📁 Project Structure

```text
retail-ai-dataset-preparation/
│
├── scripts/
│   ├── validate_dataset.py
│   ├── clean_dataset.py
│   ├── validate_coordinates.py
│   ├── validate_prices.py
│   ├── generate_report.py
│   └── run_pipeline.py
│
├── sample_data/
│   ├── sample_leaflets.csv
│   └── clean_sample_leaflets.csv
│
├── reports/
│   └── validation_report.txt
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Pipeline Workflow

```text
Retail Dataset
      │
      ▼
Dataset Validation
      │
      ▼
Data Cleaning
      │
      ▼
Coordinate Validation
      │
      ▼
Price Validation
      │
      ▼
Quality Report Generation
      │
      ▼
Clean Dataset Output
```

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/Oluwadamilola289/retail-ai-dataset-preparation.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python scripts/run_pipeline.py
```

---

## 📊 Example Output

```text
Loaded 6 rows.

Removed 0 duplicate rows.
Removed 0 completely empty rows.
Whitespace removed from text columns.
Text standardized.

Found 0 invalid bounding boxes.
Found 0 invalid prices.

Validation report generated.

DATA CLEANING COMPLETE

Duplicate rows removed : 0
Empty rows removed : 0
Invalid bounding boxes : 0
Invalid prices : 0
Final rows : 6
```

---

## 📄 Generated Files

The pipeline automatically creates:

- `clean_sample_leaflets.csv`
- `validation_report.txt`

---

## 🔮 Future Improvements

- Brand validation
- Logging
- Unit tests
- GitHub Actions (CI/CD)
- Docker support
- Cloud deployment
- Configuration file support

---

## 👩‍💻 Author

**Oluwadamilola Osho**

MSc Data Science | AI & Data Professional

GitHub: https://github.com/Oluwadamilola289