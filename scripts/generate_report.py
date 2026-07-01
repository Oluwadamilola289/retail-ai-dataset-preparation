from pathlib import Path


def generate_report(
    total_rows,
    duplicates_removed,
    empty_rows_removed,
    invalid_boxes,
    invalid_prices,
):
    """
    Generate a data quality report.
    """

    report = f"""
====================================
Retail AI Dataset Quality Report
====================================

Dataset Summary
---------------
Rows Loaded: {total_rows}

Cleaning
--------
Duplicate Rows Removed : {duplicates_removed}
Empty Rows Removed     : {empty_rows_removed}

Validation
----------
Invalid Bounding Boxes : {len(invalid_boxes)}
Invalid Prices         : {len(invalid_prices)}

Final Status
------------
"""

    if len(invalid_boxes) == 0 and len(invalid_prices) == 0:
        report += "✅ DATASET READY FOR AI TRAINING\n"
    else:
        report += "⚠️ DATASET REQUIRES REVIEW\n"

    Path("reports").mkdir(exist_ok=True)

    with open("reports/validation_report.txt", "w") as file:
        file.write(report)

    print("Validation report generated.")