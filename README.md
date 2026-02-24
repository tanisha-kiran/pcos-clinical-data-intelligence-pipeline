# 🩺 PCOS Clinical Data Intelligence Pipeline

## 📌 Project Overview

This project presents an end-to-end Clinical Data Intelligence Pipeline built using a Polycystic Ovary Syndrome (PCOS) dataset from Kaggle.

The system automates:

- Dataset ingestion
- Data preprocessing & cleaning
- Clinical feature enrichment
- Data quality validation
- Predictive modeling for PCOS classification

The goal is to demonstrate structured data engineering + analytics + machine learning workflow in a healthcare setting.

---

## 🏗 Architecture

Raw Dataset (Kaggle)
        ↓
Data Download Automation
        ↓
Preprocessing & Cleaning
        ↓
Feature Engineering (Clinical Indicators)
        ↓
Data Quality Validation
        ↓
Predictive Modeling (Logistic Regression)
        ↓
Exploratory Visualizations

---

## ⚙️ Key Features

### 🔹 1. Automated Dataset Download
- Uses KaggleHub API
- Reproducible and version-controlled data ingestion

### 🔹 2. Data Preprocessing
- Duplicate removal
- Standardized column formatting
- Missing value handling (median imputation)
- Clean structured dataset generation

### 🔹 3. Clinical Feature Engineering
Derived intelligent health indicators such as:

- BMI Category (Underweight / Normal / Overweight / Obese)
- High Insulin Risk Flag
- Hormonal Imbalance Indicator
- Validation status tracking

### 🔹 4. Data Quality Validation
Automated QA report including:
- Duplicate record detection
- Missing value summary
- Invalid BMI detection
- Structured logging

### 🔹 5. Predictive Modeling
- Logistic Regression classifier
- Train/Test split
- Accuracy & classification report
- Correlation analysis

---

## 📊 Exploratory Insights

- BMI distribution across patients
- Feature correlation with PCOS diagnosis
- Insulin and hormonal imbalance relationships

Visualizations included in the notebook:
- BMI Category Distribution
<img width="543" height="510" alt="image" src="https://github.com/user-attachments/assets/d0819fc2-ca59-4afa-908a-0d8737a1d6e4" />

- Correlation Bar Plot
  <img width="664" height="413" alt="image" src="https://github.com/user-attachments/assets/a01c44f2-864f-456e-824d-1e78af43cbe8" />


---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- KaggleHub API

---

## 🚀 How to Run the Pipeline

1️⃣ Install dependencies:
pip install -r requirements.txt


2️⃣ Run complete pipeline:
python src/download_dataset.py
python src/preprocessing.py
python src/enrichment.py
python src/quality_check.py
python src/model.py


---

## 📥 Dataset Source

PCOS Dataset – Kaggle  
Downloaded programmatically using KaggleHub API.

---

## 📈 Future Improvements

- Model comparison (Random Forest / XGBoost)
- ROC Curve & AUC analysis
- Confusion Matrix visualization
- Feature importance ranking
- Streamlit dashboard deployment
- Hyperparameter tuning

---

## ⚠ Disclaimer

This project is for educational and analytical purposes only.  
It does not provide medical diagnosis or treatment recommendations.

---

## 👩‍💻 Author

Tanisha Kiran  
Aspiring Data Scientist | AI & ML Enthusiast  
