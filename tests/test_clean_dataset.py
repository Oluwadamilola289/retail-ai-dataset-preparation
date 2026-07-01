import pandas as pd

from scripts.clean_dataset import remove_duplicates


def test_remove_duplicates():

    df = pd.DataFrame({
        "brand": ["Coke", "Coke", "Pepsi"],
        "price": [2, 2, 3]
    })

    cleaned_df, duplicates_removed = remove_duplicates(df)

    assert len(cleaned_df) == 2
    assert duplicates_removed == 1