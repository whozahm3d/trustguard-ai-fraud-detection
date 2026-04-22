# Feature scaling was applied to numerical variables using StandardScaler to normalize the distribution of transaction-related variables. 
# This step ensures that features with larger ranges do not dominate the learning process of machine learning models.

def preprocess_data(df):

    df = remove_duplicates(df)

    df = encode_transaction_type(df)

    numerical_columns = [
        "amount",
        "oldbalanceOrg",
        "newbalanceOrig",
        "oldbalanceDest",
        "newbalanceDest"
    ]

    scaler = StandardScaler()

    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    return df
preprocess_data(df)


# Fraud vs Non-Fraud distribution
# Fraud detection datasets are typically highly imbalanced,
# meaning fraudulent transactions represent a very small
# percentage of the total transactions.

fraud_counts = df["isFraud"].value_counts()

print(fraud_counts)

fraud_percentage = df["isFraud"].value_counts(normalize=True) * 100

print("\nFraud Percentage:")
print(fraud_percentage)


# ploting the data before scaling and after scaling and checking how the standard scaling affect the entire dataset.
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
# Load a fresh copy of the dataset to show 'Before Scaling'
original_df = load_dataset("/content/PaySim - Synthetic Financial Dataset for Fraud Detection.csv")
sns.histplot(original_df["amount"])
plt.title("Before Scaling")

plt.subplot(1,2,2)
sns.histplot(df["amount"])
plt.title("After Scaling")
