def dataset_shape(df):
    """
    Display number of rows and columns
    """
    print("Dataset Shape:", df.shape)
dataset_shape(df)

def dataset_columns(df):
    """
    Display column names
    """
    print("Columns:")
    print(df.columns)
dataset_columns(df)

def dataset_datatypes(df):
    """
    Display datatypes of each column
    """
    print("Data Types:")
    print(df.dtypes)
dataset_datatypes(df)

def dataset_head(df):
    """
    Display first rows
    """
    print("First 5 Rows:")
    print(df.head())
dataset_head(df)

def dataset_description(df):
    """
    Statistical summary of dataset
    """
    print("Dataset Statistical Summary:")
    print(df.describe())
dataset_description(df)

def missing_values(df):
    """
    Check missing values in dataset
    """
    print("Missing Values:")
    print(df.isnull().sum())
missing_values(df)




