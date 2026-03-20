# Running the entire dataset for the complete preprocessing and analysis of PaySim Dataset of the project

def main():

    df = load_dataset("/content/PaySim - Synthetic Financial Dataset for Fraud Detection.csv")

    dataset_shape(df)
    dataset_columns(df)
    dataset_datatypes(df)
    dataset_head(df)
    dataset_description(df)
    missing_values(df)

    df = preprocess_data(df)

    print("\nPREPROCESING COMPLETED!")


if __name__ == "__main__":
    main()
