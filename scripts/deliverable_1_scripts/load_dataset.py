# Load the PaySim dataset containing synthetic financial transaction records used for fraud detection analysis.

def load_dataset(path):
    """
    Load dataset from CSV file
    """

    df = pd.read_csv(path)

    print("Dataset Loaded Successfully")
    print("Shape:", df.shape)

    return df


if __name__ == "__main__":

    dataset_path = "/content/PaySim - Synthetic Financial Dataset for Fraud Detection.csv"

    df = load_dataset(dataset_path)

    print(df.head())
