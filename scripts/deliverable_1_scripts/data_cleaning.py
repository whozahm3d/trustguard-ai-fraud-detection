# Check for missing values to ensure data quality before performing preprocessing and analysis.

def remove_duplicates(df):
    """
    Remove duplicate rows
    """

    before = df.shape[0]

    df = df.drop_duplicates()

    after = df.shape[0]

    print("Duplicates removed:", before - after)

    return df
remove_duplicates(df)


def check_outliers(df, column):
    """
    Detect outliers using IQR
    """

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    return df[(df[column] >= lower) & (df[column] <= upper)]
check_outliers(df, "amount")

