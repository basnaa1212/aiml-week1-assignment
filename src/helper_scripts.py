import pandas as pd


def load_dataset(file_path):
    """Load a CSV dataset."""
    return pd.read_csv(file_path)


def show_dataset_summary(df):
    """Display basic dataset information."""
    print("Dataset shape:", df.shape)
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())
