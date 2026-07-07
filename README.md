# Phishing Website Detection using Machine Learning

## Project Description

This project reproduces and critically evaluates a published machine learning solution for phishing website detection.

The objective is to classify websites as either **phishing** or **legitimate** using handcrafted features extracted from URLs and website characteristics.

In addition to reproducing the original work, this project extends the evaluation by implementing additional machine learning models and performing a more comprehensive performance analysis.

---

## Project Tasks

The project includes:

- Exploratory Data Analysis (EDA)
- Correlation Analysis
- Feature Importance Analysis
- Class Distribution Analysis
- Training and evaluation of multiple machine learning models
- Model comparison
- ROC Curve Analysis
- Precision–Recall Curve Analysis
- Threshold Analysis
- Critical evaluation of the original project

---

## Implemented Models

The following machine learning models were implemented and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- Multilayer Perceptron (MLP)
- XGBoost

---

## Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- F2-score
- Matthews Correlation Coefficient (MCC)
- ROC-AUC
- PR-AUC
- Confusion Matrix

Additional evaluation includes:

- ROC Curve Comparison
- Precision–Recall Curve Comparison
- Threshold Analysis

---

## Original Project

This project is based on the following GitHub repository:

https://github.com/shreyagopal/Phishing-Website-Detection-by-Machine-Learning-Techniques

---

## Repository Contents

```text
Phishing_Website_Detection_using_Machine_Learning.ipynb
Phishing_Website_Detection_Report.pdf
5.urldata.csv
requirements.txt
README.md
results/
```

The **results/** folder contains:

- Confusion matrices
- ROC Curve Comparison
- Precision–Recall Curve Comparison
- Precision vs Decision Threshold
- Recall vs Decision Threshold
- Feature Importance
- Correlation Matrix
- Class Distribution
- Comparison Table

---

## Requirements

The project was developed using **Python 3**.

Install the required libraries using:

```bash
pip install -r requirements.txt
```

---

## Execution Instructions

1. Clone or download this repository.
2. Make sure that **5.urldata.csv** is located in the same folder as the notebook.
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Open the Jupyter Notebook.
5. Run all notebook cells from top to bottom.

---

## Dataset

The dataset contains **10,000 websites**:

- 5,000 phishing websites collected from **PhishTank**
- 5,000 legitimate websites collected from the **University of New Brunswick (UNB)**

The dataset included in this repository is:

```
5.urldata.csv
```

Original sources:

PhishTank:
https://www.phishtank.com/

University of New Brunswick (UNB):
https://www.unb.ca/cic/datasets/url-2016.html

---

## Results Summary

Six machine learning models were evaluated using multiple evaluation metrics.

Among all evaluated models, **XGBoost** achieved the best overall performance across Accuracy, F1-score, MCC, and PR-AUC while also achieving one of the highest ROC-AUC values.

Random Forest achieved very similar results, making both ensemble models the strongest classifiers for phishing website detection.

The project also includes:

- Exploratory Data Analysis
- Feature Importance Analysis
- Correlation Analysis
- Class Distribution Analysis
- ROC Curve Analysis
- Precision–Recall Curve Analysis
- Threshold Analysis
- Critical evaluation of the original project

---

## Author

This repository was created as part of the **Data Science in Cybersecurity** course at the **University of Haifa**.
