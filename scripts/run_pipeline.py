from validate_coordinates import validate_coordinates
from validate_prices import validate_prices
from generate_report import generate_report
from load_config import load_config
from logger import setup_logger
from generate_metrics import generate_metrics
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
    logger = setup_logger()

    logger.info("Retail AI Pipeline Started")
    config = load_config()

    df = pd.read_csv(config["input_file"])

    logger.info(f"Loaded {len(df)} rows.")

    # Cleaning pipeline
    df, duplicates_removed = remove_duplicates(df)

    df, empty_rows_removed = remove_empty_rows(df)

    df = trim_whitespace(df)

    df = standardize_text(df)

    invalid_boxes = validate_coordinates(df)
    invalid_prices = validate_prices(df)

    

    # Save cleaned dataset
    save_clean_dataset(
    df,
    config["output_file"]
    )
    generate_report(
       total_rows=len(df),
       duplicates_removed=duplicates_removed,
       empty_rows_removed=empty_rows_removed,
       invalid_boxes=invalid_boxes,
       invalid_prices=invalid_prices,
    )
    generate_metrics(
    total_rows=len(df),
    duplicates_removed=duplicates_removed,
    empty_rows_removed=empty_rows_removed,
    invalid_boxes=invalid_boxes,
    invalid_prices=invalid_prices,
    )
    logger.info("Quality metrics generated.")
    logger.info("Validation report generated.")
    logger.info("Pipeline completed successfully.")
    print("\n================================")
    print("DATA CLEANING COMPLETE")
    print("================================")
    print(f"Duplicate rows removed : {duplicates_removed}")
    print(f"Empty rows removed     : {empty_rows_removed}")
    print(f"Invalid bounding boxes : {len(invalid_boxes)}")
    print(f"Invalid prices         : {len(invalid_prices)}")
    print(f"Final rows             : {len(df)}")
    logger.info(f"Duplicate rows removed: {duplicates_removed}")
    logger.info(f"Empty rows removed: {empty_rows_removed}")
    logger.info(f"Invalid bounding boxes: {len(invalid_boxes)}")
    logger.info(f"Invalid prices: {len(invalid_prices)}")

if __name__ == "__main__":
    
    main()