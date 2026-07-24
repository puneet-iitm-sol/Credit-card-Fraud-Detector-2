# 💳 Credit Card Fraud Detection

A machine learning project for detecting fraudulent credit card transactions using multiple classification algorithms. The project focuses on handling highly imbalanced data, comparing model performance, and evaluating results with metrics suitable for fraud detection.

---

## 📌 Project Overview

Credit card fraud detection is a binary classification problem where the objective is to identify fraudulent transactions while minimizing false alarms. Since fraudulent transactions make up only a small fraction of the dataset, special techniques are required to build an effective model.

This project analyzes **284,807 anonymized credit card transactions**, where only **0.17%** of the transactions are fraudulent.

---

## 🎯 Objectives

* Detect fraudulent credit card transactions with high recall.
* Handle severe class imbalance effectively.
* Compare the performance of multiple machine learning models.
* Evaluate models using appropriate classification metrics.
* Visualize model performance for better interpretation.

---

## 📊 Dataset

* **Total Transactions:** 284,807
* **Fraudulent Transactions:** 492
* **Fraud Rate:** 0.17%

The dataset contains anonymized features (`V1`–`V28`), transaction **Time**, **Amount**, and the target variable **Class**, where:

* **0** → Legitimate Transaction
* **1** → Fraudulent Transaction

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* imbalanced-learn (SMOTE)

---

## ⚙️ Machine Learning Pipeline

1. Load and inspect the dataset.
2. Perform exploratory data analysis (EDA).
3. Preprocess and prepare the data.
4. Address class imbalance using **SMOTE**.
5. Split the dataset into training and testing sets.
6. Train multiple machine learning models:

   * Logistic Regression
   * Random Forest
   * XGBoost
7. Evaluate model performance using classification metrics.
8. Visualize results using confusion matrices, ROC curves, and Precision-Recall curves.

---

## 📈 Models Compared

* Logistic Regression
* Random Forest Classifier
* XGBoost Classifier

The models were compared using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC Score

---

## 📊 Results

* Successfully analyzed **284,807** anonymized credit card transactions.
* Improved **ROC-AUC** to **0.98+** through model comparison and optimization.
* Addressed severe class imbalance using **SMOTE**, increasing fraud recall from approximately **38%** to **81%**.
* Evaluated model performance using confusion matrices and Precision-Recall (PR) and ROC curves to achieve an effective balance between precision and recall.

---

## 📉 Visualizations

The project includes:

* Class distribution
* Correlation heatmap
* Confusion Matrix
* ROC Curve
* Precision-Recall Curve
* Model performance comparison

---

## 🚀 Future Improvements

* Hyperparameter tuning with GridSearchCV or RandomizedSearchCV.
* Real-time fraud prediction using a REST API.
* Model deployment using Flask or FastAPI.
* Experiment with ensemble and deep learning approaches.
* Implement model monitoring and retraining for production environments.

---

## 📚 Key Concepts Demonstrated

* Binary Classification
* Imbalanced Data Handling
* SMOTE Oversampling
* Feature Scaling
* Model Comparison
* Performance Evaluation
* Precision-Recall Trade-off
* ROC-AUC Analysis

---

## 📌 Project Highlights

* Analyzed **284,807** anonymized credit card transactions.
* Compared **Logistic Regression**, **Random Forest**, and **XGBoost** models.
* Improved **ROC-AUC** to **0.98+**.
* Increased fraud detection recall from **38%** to **81%** using **SMOTE**.
* Visualized confusion matrices, ROC curves, and Precision-Recall curves for comprehensive model evaluation.

---

## 👨‍💻 Author

Developed as a machine learning project to explore fraud detection techniques on highly imbalanced datasets and compare the performance of multiple classification algorithms.
