import pandas as pd

from clean_dataset import (
    remove_duplicates,
    remove_empty_rows,
    trim_whitespace,
    standardize_text,
    save_clean_dataset,
)


def main():

    # Load dataset
    df = pd.read_csv("sample_data/sample_leaflets.csv")

    print(f"Loaded {len(df)} rows.\n")

    # Cleaning pipeline
    df, duplicates_removed = remove_duplicates(df)

    df, empty_rows_removed = remove_empty_rows(df)

    df = trim_whitespace(df)

    df = standardize_text(df)

    # Save cleaned dataset
    save_clean_dataset(
        df,
        "sample_data/clean_sample_leaflets.csv"
    )

    print("\n================================")
    print("DATA CLEANING COMPLETE")
    print("================================")
    print(f"Duplicate rows removed : {duplicates_removed}")
    print(f"Empty rows removed     : {empty_rows_removed}")
    print(f"Final rows             : {len(df)}")


if __name__ == "__main__":
    main()