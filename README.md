# 📊 Retail AI Dataset Preparation Pipeline

A production-style Python data preparation pipeline that cleans, validates, and monitors retail product datasets before AI model training.

The project demonstrates modern data engineering practices including automated data validation, structured logging, configuration management, unit testing, GitHub Actions CI/CD, quality metrics generation, and an interactive Streamlit dashboard.
---

---

## ✨ Features

- Clean retail datasets using reusable Python modules
- Remove duplicate records
- Remove completely empty rows
- Trim whitespace and standardize text
- Validate bounding box coordinates
- Validate product prices
- Generate validation reports
- Generate JSON quality metrics
- Structured logging
- Interactive Streamlit dashboard
- Unit testing with Pytest
- Automated GitHub Actions CI
---

---
## 🏗️ Pipeline Architecture

```text
Raw CSV
    │
    ▼
Load Dataset
    │
    ▼
Data Cleaning
    │
    ▼
Data Validation
    │
    ▼
Reports & Metrics
    │
    ▼
Streamlit Dashboard
```
---

---

## 📁 Project Structure

```text
retail-ai-dataset-preparation/
│
├── config/
├── images/
├── logs/
├── reports/
├── sample_data/
├── scripts/
├── tests/
├── dashboard.py
├── requirements.txt
└── README.md
```
---

---
## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Oluwadamilola289/retail-ai-dataset-preparation.git

cd retail-ai-dataset-preparation
```

Install dependencies

```bash
pip install -r requirements.txt
```
---

---

## ▶️ Run the Pipeline

```bash
python scripts/run_pipeline.py
```

Outputs generated:

- reports/validation_report.txt
- reports/quality_metrics.json
- logs/pipeline.log
---

---
## 📊 Launch Dashboard

```bash
streamlit run dashboard.py
```
---

---
## 🛠️ Technologies

- Python
- Pandas
- Streamlit
- Pytest
- Git
- GitHub Actions
- JSON
---

---
## 🚀 Future Improvements

- Docker containerization
- Database integration
- Scheduled pipeline execution
- Cloud deployment
- Additional validation rules
- Email notifications
---

---
## 👩‍💻 Author

**Oluwadamilola Osho**

Data Analyst | AI Engineer | Machine Learning Enthusiast

GitHub:
https://github.com/Oluwadamilola289

