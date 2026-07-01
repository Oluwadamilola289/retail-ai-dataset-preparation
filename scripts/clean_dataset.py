import pandas as pd


def remove_duplicates(df):
    """
    Remove duplicate rows from the dataset.
    """

    rows_before = len(df)

    cleaned_df = df.drop_duplicates()

    rows_after = len(cleaned_df)

    duplicates_removed = rows_before - rows_after

    print(f"Removed {duplicates_removed} duplicate rows.")

    return cleaned_df, duplicates_removed


def remove_empty_rows(df):
    """
    Remove rows where all columns are empty.
    """

    rows_before = len(df)

    cleaned_df = df.dropna(how="all")

    rows_after = len(cleaned_df)

    empty_rows_removed = rows_before - rows_after

    print(f"Removed {empty_rows_removed} completely empty rows.")

    return cleaned_df, empty_rows_removed

def trim_whitespace(df):
    """
    Remove leading and trailing whitespace from text columns.
    """

    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    print("Whitespace removed from text columns.")

    return df    

def standardize_text(df):
    """
    Standardize text formatting.
    """

    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.title()

    print("Text standardized.")

    return df
def save_clean_dataset(df, output_path):
    """
    Save cleaned dataset to a CSV file.
    """

    df.to_csv(output_path, index=False)

    print(f"Clean dataset saved to {output_path}")