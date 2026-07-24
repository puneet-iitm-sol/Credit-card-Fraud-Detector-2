## 📂 Project Structure

```text
Credit-card-Fraud-Detector-2/
│
├── data/
│   └── creditcard.csv                # Dataset
│
├── notebooks/
│   └── Credit_Card_Fraud_Detection.ipynb
│
├── src/
│   ├── data_preprocessing.py         # Data cleaning & preprocessing
│   ├── train_model.py                # Model training
│   ├── evaluate_model.py             # Model evaluation
│   ├── visualization.py              # ROC, PR curves & confusion matrix
│   └── utils.py                      # Helper functions
│
├── models/
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   └── xgboost_model.pkl
│
├── images/
│   ├── class_distribution.png
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   ├── precision_recall_curve.png
│   └── feature_importance.png
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── main.py
```
