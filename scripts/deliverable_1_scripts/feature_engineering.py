def encode_transaction_type(df):
    """
    Convert transaction type into numeric values
    """

    encoder = LabelEncoder()

    df["type"] = encoder.fit_transform(df["type"])

    return df
encode_transaction_type(df)


