import pandas as pd

def analyze_dataset(df, target_column):

    rows = df.shape[0]
    cols = df.shape[1]

    missing = df.isnull().sum().sum()

    missing_percent = (
        missing / (rows * cols)
    ) * 100

    numeric = len(
        df.select_dtypes(
            include=["int64", "float64"]
        ).columns
    )

    categorical = len(
        df.select_dtypes(
            include=["object", "category"]
        ).columns
    )

    if str(df[target_column].dtype) == "object":
        target_type = "Classification"
    else:
        target_type = "Regression"

    return {
        "rows": rows,
        "cols": cols,
        "missing_percent": round(
            missing_percent,
            2
        ),
        "numeric": numeric,
        "categorical": categorical,
        "target_type": target_type
    }