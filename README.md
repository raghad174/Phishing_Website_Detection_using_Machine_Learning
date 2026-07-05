# Phishing Website Detection using Machine Learning

## Project Description

This project reproduces and critically evaluates a published machine learning solution for phishing website detection.

The objective is to classify websites as either **phishing** or **legitimate** using features extracted from URLs and website characteristics.

As part of this project, I performed:

- Exploratory Data Analysis (EDA)
- Correlation Analysis
- Feature Importance Analysis
- Class Distribution Analysis
- Training and evaluation of multiple machine learning models
- Model comparison
- Critical evaluation of the original work

---

## Implemented Models

The following machine learning models were implemented and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- Multilayer Perceptron (MLP)
- XGBoost

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

## Original Project

This project is based on the following GitHub repository:

https://github.com/shreyagopal/Phishing-Website-Detection-by-Machine-Learning-Techniques

---

## Repository Contents

- Phishing_Website_Detection_using_Machine_Learning.ipynb
- Phishing Website Detection using Machine Learning Techniques.pdf
- 5.urldata.csv
- requirements.txt
- README.md

---

## Requirements

The project was developed using **Python 3**.

Install all required libraries using:

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

Six machine learning models were evaluated for phishing website detection.

Among the evaluated models, **XGBoost** achieved the best overall performance with the highest Accuracy and F1-score.

Random Forest and Decision Tree also achieved strong performance, while Support Vector Machine obtained the highest Precision.

The project also includes exploratory data analysis, feature importance analysis, class imbalance discussion, and a critical evaluation of the original study.

---

## Author

This repository was created as part of a university assignment on phishing website detection using machine learning.
