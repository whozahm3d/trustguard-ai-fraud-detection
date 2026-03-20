# Perform visual analysis to understand patterns in transactions and identify potential fraud indicators.

# 1. Transaction Volume Over Time
# Concept: Detect seasonal or temporal trends in transaction activity. Sudden spikes may indicate fraud bursts.
# Technical Insight: Use time-series aggregation of transaction counts by day/week/month.

# The 'transaction_date' column does not exist. Using 'step' as a proxy for time.
time_series = df.groupby('step').size()

plt.figure(figsize=(12,5))
plt.plot(time_series, marker='o')
plt.title('Transaction Volume Over Time (by Step)')
plt.xlabel('Step')
plt.ylabel('Number of Transactions')
plt.savefig("../images/transaction_volume_over_time.png", dpi=300, bbox_inches="tight")
plt.show()


# 2. Fraudulent vs Legitimate Transaction Distribution
# Concept: Compare class imbalance visually. Essential for imbalanced classification problems.
# Technical Insight: Bar charts or pie charts for categorical understanding.

def fraud_distribution(df):

    plt.figure(figsize=(6,4))
    sns.countplot(x="isFraud", data=df)

    plt.title("Fraud vs Non-Fraud Transactions")

    plt.savefig("../images/fraud_distribution.png")
  
os.makedirs('../images', exist_ok=True)
fraud_distribution(df)


# 3. Transaction types Distribution
def transaction_types(df):

    plt.figure(figsize=(8,5))
    sns.countplot(x="type", data=df)

    plt.title("Transaction Types Distribution")

    plt.savefig("../images/transaction_types_distribution.png")

os.makedirs('../images', exist_ok=True)
transaction_types(df)

# 4. Fraud Transaction by Type
plt.figure(figsize=(8,5))

sns.countplot(x="type", hue="isFraud", data=df)

plt.title("Fraud Transactions by Type")

plt.savefig("../images/fraud_by_transaction_type.png", dpi=300, bbox_inches="tight")

plt.show()

# 5. Transaction Amount Distribution
# Visualizing transaction amount distribution helps understand
# skewness and the need for feature scaling.

plt.figure(figsize=(8,5))

sns.histplot(df["amount"], bins=50)

plt.title("Transaction Amount Distribution")

plt.savefig("../images/transaction_amount_distribution.png", dpi=300, bbox_inches="tight")

plt.show()


# 6. Transaction Amount Distribution by Fraud Status
# Concept: Fraud often shows unusual transaction amounts.
# Technical Insight: Boxplots or violin plots highlight outliers and distribution skew.

sns.boxplot(x='isFraud', y='amount', data=df)
plt.title('Transaction Amount Distribution by Fraud Status')
plt.savefig("../images/fraud_vs_normal_transaction_amounts.png", dpi=300, bbox_inches="tight")
plt.show()


# 7. Correlation Heatmap
# Concept: Identify relationships between numeric features; helps detect potential predictive features.
# Technical Insight: Strong correlations can guide feature engineering or indicate redundancy.

def correlation_heatmap(df):

    plt.figure(figsize=(10,8))

    # Select only numerical columns for correlation calculation
    numerical_df = df.select_dtypes(include=[np.number])
    sns.heatmap(numerical_df.corr(), cmap="rocket", annot=True, fmt=".2f")

    plt.title("Feature Correlation Heatmap")

    plt.savefig("../images/correlation_heatmap.png")

os.makedirs('../images', exist_ok=True)
correlation_heatmap(df)

# 8. Feature Importance using Correlation (No ML model needed)

features = df.drop(columns=['nameOrig', 'nameDest', 'isFraud', 'isFlaggedFraud'])

importances = features.corrwith(df['isFraud']).abs().sort_values()

importances.plot(kind='barh', figsize=(10, 7), color='teal')
plt.title('Feature Importance for Fraud Detection')
plt.savefig("../images/feature_importance.png", dpi=300, bbox_inches="tight")
plt.show()


## Key Insights from EDA

# - The dataset is highly imbalanced with fraudulent transactions representing a very small percentage.
# - Certain transaction types such as TRANSFER and CASH_OUT show higher fraud occurrences.
# - Transaction amounts show skewed distribution indicating the presence of large financial transfers.
# - Feature scaling was necessary to normalize transaction-related variables.
