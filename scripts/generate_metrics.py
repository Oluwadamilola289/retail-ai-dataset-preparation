import json
import os


def generate_metrics(
    total_rows,
    duplicates_removed,
    empty_rows_removed,
    invalid_boxes,
    invalid_prices,
):
    """
    Generate a JSON file containing pipeline quality metrics.
    """

    os.makedirs("reports", exist_ok=True)

    quality_score = 100

    quality_score -= duplicates_removed
    quality_score -= empty_rows_removed
    quality_score -= len(invalid_boxes)
    quality_score -= len(invalid_prices)

    quality_score = max(0, quality_score)

    metrics = {
        "rows_loaded": total_rows,
        "duplicates_removed": duplicates_removed,
        "empty_rows_removed": empty_rows_removed,
        "invalid_bounding_boxes": len(invalid_boxes),
        "invalid_prices": len(invalid_prices),
        "quality_score": quality_score,
        "status": (
            "READY FOR MODEL TRAINING"
            if quality_score >= 95
            else "REVIEW REQUIRED"
        ),
    }

    with open("reports/quality_metrics.json", "w") as file:
        json.dump(metrics, file, indent=4)

    return metrics