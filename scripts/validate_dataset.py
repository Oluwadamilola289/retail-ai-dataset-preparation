import pandas as pd
from pathlib import Path
# Create the validation function
def validate_dataset(file_path):
    """
    Validate a retail dataset before AI model training.
    """

    df = pd.read_csv(file_path)

    print("=" * 50)
    print("RETAIL DATASET VALIDATION REPORT")
    print("=" * 50)
    # Add some useful information
    print(f"\nRows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumn Names")
    print(df.columns.tolist())

    # Check for missing values
    print("\nMissing Values")
    print(df.isnull().sum())

    # Check duplicates
    duplicates = df.duplicated().sum()

    print(f"\nDuplicate Rows: {duplicates}")

    # Finish the script
    print("\nValidation Complete")

    
if __name__ == "__main__":
    sample_file = Path("sample_data/sample_leaflets.csv")

    if sample_file.exists():
        validate_dataset(sample_file)
    else:
        print("Sample dataset not found.")