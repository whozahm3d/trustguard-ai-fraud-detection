# TrustGuard AI: Explainable Fraud Detection for Digital Banking with RAG-Based Policy Assistance

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Pandas](https://img.shields.io/badge/Pandas-2.0-green) ![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-1.3-orange) ![Status](https://img.shields.io/badge/Status-Deliverable%201%20Complete-brightgreen)

---

## Description

Financial fraud is a growing threat in the digital banking era, costing institutions and individuals trillions of dollars each year. TrustGuard AI is an end-to-end AI-powered fraud detection system that uses machine learning to identify suspicious financial transactions and integrates **Explainable AI (XAI)** to provide transparent, interpretable reasoning behind every prediction. A **Retrieval-Augmented Generation (RAG) policy assistant** will further enhance the system by retrieving relevant banking regulations and fraud policies to explain why certain transactions are flagged — making TrustGuard AI both accurate and accountable.

This repository contains **Deliverable 1**, covering the complete data acquisition, preprocessing pipeline, and exploratory data analysis on the PaySim synthetic financial dataset.

---

## Problem Statement

Financial institutions process millions of digital transactions daily. Identifying fraudulent activity is challenging because fraud patterns evolve continuously and often closely resemble legitimate behavior. Traditional rule-based systems struggle to detect new and sophisticated fraud strategies, frequently producing high false-positive rates that overwhelm fraud analysts.

TrustGuard AI addresses this by developing a machine learning-based framework that learns hidden behavioral patterns in transaction data, detects anomalies with higher accuracy, and provides transparent, explainable decisions — meeting both operational and regulatory requirements.

---

## Objectives

- **Data Preprocessing:** Load, inspect, clean, and prepare the PaySim dataset for analysis.
- **Exploratory Data Analysis:** Visualize transaction patterns and uncover key fraud signals.
- **Feature Engineering:** Encode categorical variables and scale numerical features for model readiness.
- **Fraud Detection Model:** Train and evaluate machine learning classifiers to identify fraudulent transactions.
- **Explainability:** Apply SHAP and LIME to make model predictions interpretable and transparent.
- **RAG Policy Assistant:** Retrieve relevant fraud regulations and generate policy-grounded explanations.
- **Web Interface:** Deploy a real-time fraud monitoring dashboard for analysts and institutions.

---

## Dataset

This project uses the **PaySim Synthetic Financial Dataset for Fraud Detection**, available on Kaggle.

> Dataset Link: [Kaggle — Synthetic Financial Datasets for Fraud Detection](https://www.kaggle.com/datasets/ealaxi/paysim1)

PaySim simulates real-world mobile money transactions calibrated against private data from an African mobile payment service. It provides a realistic and privacy-preserving environment for training fraud detection models.

| Property | Value |
|---|---|
| Total Transactions | 6,362,620 |
| Total Features | 11 |
| Fraudulent Transactions | 8,213 (0.13%) |
| Fraud Transaction Types | TRANSFER, CASH_OUT only |
| Missing Values | None |
| Duplicate Records | None |

**Key Features:**

| Column | Description |
|---|---|
| `step` | Simulated time unit (1 step = 1 hour) |
| `type` | Transaction type (CASH-IN, CASH-OUT, DEBIT, PAYMENT, TRANSFER) |
| `amount` | Transaction amount in local currency |
| `oldbalanceOrg` | Originating account balance before transaction |
| `newbalanceOrig` | Originating account balance after transaction |
| `oldbalanceDest` | Destination account balance before transaction |
| `newbalanceDest` | Destination account balance after transaction |
| `isFraud` | Target label: 1 = Fraudulent, 0 = Legitimate |

> **Note:** The raw dataset is not included in this repository due to size. Download it from the link above and place it in `data/raw/`.

---

## Project Structure

```
trustguard-ai-fraud-detection
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── data
│   ├── raw
│   │   └── (dataset not included — see dataset_link.txt)
│   ├── processed
│   │   └── (dataset not included beacuse the file is very large — upload some of the rows and cokumns of the preprocess data)
│   └── dataset_link.txt
│
├── scripts
│   ├── load_dataset.py
│   ├── basic_inspection.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── preprocessing_pipeline.py
│   ├── eda_analysis.py
│   └── run_pipeline.py
│   └── save_cleaned_dataset.py
│
├── notebooks
│   ├── deliverable1_pipeline.ipynb
│   └── exploratory_data_analysis.ipynb
│
├── images
│   ├── transaction_volume_over_time.png
│   ├── fraud_distribution.png
│   ├── transaction_types.png
│   ├── fraud_vs_normal_transaction_amounts.png
│   ├── feature_importance.png
│   ├── fraud_by_transaction_type.png
│   ├── transaction_amount_distribution.png
│   ├── correlation_heatmap.png
│
├── reports
│   ├── Fraud_Detection_Deliverable 1_Report.pdf
│  └── Fraud_Detection_Deliverable 1_Report.doc

```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/trustguard-ai-fraud-detection.git
cd trustguard-ai-fraud-detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 3. Download the Dataset

Download the PaySim dataset from [Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1) and place the CSV file in the `data/raw/` directory:

```
data/raw/PaySim - Synthetic Financial Dataset for Fraud Detection.csv
```

---

## Usage

### Run the Full Preprocessing Pipeline

```bash
python scripts/run_pipeline.py
```

This will execute all pipeline stages in sequence:
1. Load the dataset
2. Inspect shape, types, and statistics
3. Remove duplicates and handle outliers
4. Encode the `type` column using LabelEncoder
5. Scale numerical features using StandardScaler
6. Export the processed dataset to `data/processed/processed_paysim.csv`

### Run EDA Only

```bash
python scripts/eda_analysis.py
```

### Use the Notebooks

Open the notebooks in Jupyter, Google Colab or vs code:

```bash
jupyter notebook notebooks/deliverable1_pipeline.ipynb
jupyter notebook notebooks/exploratory_data_analysis.ipynb
```

---

## Results — Exploratory Data Analysis

The EDA uncovered the following key fraud patterns in the PaySim dataset:

### Transaction Volume Over Time
![Transaction Volume Over Time](Images/deliverable_1_images/transaction_volume_over_time.png)
> A strong diurnal cycle is visible — transaction volumes peak every ~24 steps. Sudden spikes outside this rhythm may signal abnormal batch activity.

### Fraud vs. Legitimate Class Distribution
![Fraud Distribution](Images/deliverable_1_images/fraud_distribution.png)
> Only **0.13%** of transactions are fraudulent (8,213 of 6.36M). This severe imbalance means standard accuracy is a misleading metric — AUPRC and F1-score must be used.

### Transaction Type Distribution
![Transaction Types](Images/deliverable_1_images/transaction_types_distribution.png)
> PAYMENT and CASH_OUT are the most frequent types. However, volume alone does not reflect fraud risk.

### Fraud Concentration by Transaction Type
![Fraud by Transaction Type](Images/deliverable_1_images/fraud_by_transaction_type.png)
> **Fraud occurs exclusively in TRANSFER and CASH_OUT transactions.** This allows a pre-filter that eliminates ~55% of records from fraud modelling with zero loss in recall.

### Transaction Amount Distribution
![Transaction Amount Distribution](Images/deliverable_1_images/transaction_amount_distribution.png)
> Heavily right-skewed — most transactions are below 500K but a tail extends to ~92M. Feature scaling is essential.

### Transaction Amount: Fraud vs. Legitimate
![Fraud vs Normal Amounts](Images/deliverable_1_images/fraud_vs_normal_transaction_amounts.png)
> Fraudulent transactions cluster at higher amounts with a broader spread, confirming large amounts as a key fraud signal.

### Feature Correlation Matrix
![Correlation Heatmap](Images/deliverable_1_images/correlation_heatmap.png)
> Balance features are strongly inter-correlated. `isFlaggedFraud` shows near-zero correlation with actual fraud — it must be excluded from model features.

### Feature Importance (Correlation with Fraud Label)
![Feature Importance](Images/deliverable_1_images/feature_importance.png)
> `oldbalanceOrg` and `newbalanceOrig` are the strongest predictors — fraudulent transactions characteristically drain the originating account to zero (the **balance-drain signature**).

---

## Contributors

- Shahzeb Imran
- Taha Nawaz
- Ali Ahmad

---

## Academic Integrity

This project is developed as part of an academic AI course at the **National University of Computer and Emerging Sciences (NUCES), Lahore**. All contributors are expected to fully understand the implementation and be prepared to explain the system during evaluation. AI tools may be used for assistance but not as a substitute for understanding.

---

*Department of Computer Science — NUCES Lahore | Fall 2024*
