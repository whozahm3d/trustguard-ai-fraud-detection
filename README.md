# Explainable AI-Driven Financial Fraud Detection with RAG Policy Assistant

## Project Overview

The rapid growth of digital banking and mobile payment services has significantly increased the risk of financial fraud. Traditional rule-based fraud detection systems often fail to detect complex fraud patterns hidden within large volumes of transaction data.

This project aims to build an **AI-powered financial fraud detection system** that uses machine learning to identify suspicious financial transactions and integrates **Explainable AI (XAI)** to provide transparent reasoning behind predictions. In addition, a **Retrieval-Augmented Generation (RAG) policy assistant** will retrieve relevant banking regulations and fraud policies to explain why certain transactions are flagged.

The system is designed as an **end-to-end AI pipeline**, covering data preprocessing, model training, fraud prediction, explainability, and policy-based explanations through a RAG framework.

---

# Objectives

The primary objectives of this project are:

* Detect fraudulent financial transactions using machine learning
* Improve interpretability of predictions using Explainable AI techniques
* Integrate a RAG system to retrieve relevant fraud regulations and policy explanations
* Build a scalable AI pipeline that can be extended to real banking systems
* Develop a web-based interface for fraud monitoring and analysis

---

# Problem Statement

Financial institutions process millions of digital transactions daily. Identifying fraudulent activity within these transactions is challenging because fraud patterns evolve continuously and often resemble legitimate behavior.

Traditional rule-based systems struggle to detect new fraud strategies and often produce high false-positive rates. Machine learning models can learn hidden behavioral patterns in transaction data and detect anomalies more effectively.

This project develops an AI-based fraud detection framework capable of learning transaction patterns, identifying suspicious behavior, and providing transparent explanations for automated decisions.

---

# Target Users

This system is designed for:

* Financial institutions
* Digital banking platforms
* Fraud investigation teams
* Regulatory compliance officers
* FinTech startups building fraud detection systems

---

# Dataset

This project uses the **PaySim Synthetic Financial Dataset for Fraud Detection**.

Dataset Source:
Kaggle – Synthetic Financial Datasets for Fraud Detection (PaySim)

The dataset simulates **mobile money transactions**, including:

* Transfers
* Cash withdrawals
* Deposits
* Payments
* Fraudulent activities

### Key Features

* Transaction Type
* Transaction Amount
* Origin Account Balance
* Destination Account Balance
* Fraud Labels

This dataset provides a realistic simulation of financial transaction behavior suitable for training fraud detection models.

---

# Project Architecture

The project follows a **data-centric AI pipeline**.

```
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Feature Engineering
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Fraud Detection Model
     │
     ▼
Explainable AI Layer
     │
     ▼
RAG Policy Assistant
     │
     ▼
Web Interface
```

---

# Repository Structure

```
fraud-detection-ai-system
│
├── README.md
├── .gitignore
│
├── data
│   └── dataset_link.txt
│
├── data_scripts
│   ├── load_data.py
│   ├── data_cleaning.py
│   ├── preprocessing.py
│   └── eda.py
│
├── notebooks
│   └── exploratory_analysis.ipynb
│
├── reports
│   └── deliverable1.tex
│
└── images
    └── eda_plots
```

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* PyTorch / TensorFlow (for advanced models)
* FAISS / ChromaDB (for RAG retrieval)
* FastAPI (backend)
* Streamlit / React (frontend)

---

# Deliverables

The project will be completed in multiple stages:

### Deliverable 1

Problem Definition and Data Acquisition

Includes:

* Dataset collection
* Data preprocessing
* Exploratory Data Analysis

### Deliverable 2

Model Development

Includes:

* Feature engineering
* Fraud detection models
* Model evaluation

### Deliverable 3

Explainable AI + RAG Integration

Includes:

* Model explainability
* Policy retrieval system
* Fraud explanation interface

### Final Deliverable

Full AI System Deployment

Includes:

* Backend API
* Web application
* Real-time fraud detection interface

---

# Setup Instructions

### 1 Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 2 Clone Repository

```bash
git clone https://github.com/your-username/fraud-detection-ai-system.git
cd fraud-detection-ai-system
```

### 3 Download Dataset
Download the dataset from Kaggle and place it in the `https://www.kaggle.com/code/gpreda/synthetic-financial-datasets-data-exploration` directory.

---

# Academic Integrity

This project is developed as part of an academic AI course. AI tools may be used for assistance, but all contributors must fully understand the implementation and be able to explain the system during evaluation.

---

# Contributors
Add your group members here:

* Shahzeb Imran
* Taha Nawaz
* Ali Ahmad
