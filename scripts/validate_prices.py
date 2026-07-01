import pandas as pd


def validate_prices(df):
    """
    Validate product prices.
    """

    invalid_prices = []

    for index, row in df.iterrows():

        price = row["price"]

        if pd.isna(price):
            invalid_prices.append(index)
            continue

        if not isinstance(price, (int, float)):
            invalid_prices.append(index)
            continue

        if price <= 0:
            invalid_prices.append(index)

    print(f"Found {len(invalid_prices)} invalid prices.")

    return invalid_prices