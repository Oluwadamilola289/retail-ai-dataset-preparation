import pandas as pd


def validate_coordinates(df):
    """
    Validate bounding box coordinates.
    """

    invalid_boxes = []

    for index, row in df.iterrows():
        print(
           f"Row {index}: "
           f"x1={row['x1']} ({type(row['x1'])}), "
           f"x2={row['x2']} ({type(row['x2'])})"
        )

        if row["x1"] >= row["x2"]:
            invalid_boxes.append(index)
            continue

        if row["y1"] >= row["y2"]:
            invalid_boxes.append(index)
            continue

        if row["x1"] < 0 or row["y1"] < 0:
            invalid_boxes.append(index)
            continue

        if row["x2"] < 0 or row["y2"] < 0:
            invalid_boxes.append(index)

    print(f"Found {len(invalid_boxes)} invalid bounding boxes.")

    return invalid_boxes