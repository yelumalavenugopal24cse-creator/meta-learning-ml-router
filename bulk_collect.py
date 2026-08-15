import openml
import pandas as pd

from router.analyzer import analyze_dataset
from router.benchmark import benchmark_models
from router.meta_generator import save_meta_features

# First 50 dataset IDs to try
dataset_ids = [
    61, 37, 50, 54, 151,
    188, 38, 44, 46, 182,
    300, 307, 469, 554, 1464,
    1485, 1486, 1487, 1489, 1494,
    1497, 1501, 1504, 1507, 1510,
    1515, 1518, 1590, 1596, 179,
    181, 183, 184, 185, 186,
    187, 32, 28, 29, 30,
    31, 39, 40, 41, 42,
    43, 47, 49, 52, 53
]

for dataset_id in dataset_ids:

    try:

        print(f"\nProcessing {dataset_id}")

        dataset = openml.datasets.get_dataset(
            dataset_id
        )

        target = dataset.default_target_attribute

        if target is None:
            continue

        X, y, _, _ = dataset.get_data(
            target=target
        )

        if X.shape[0] < 50:
            continue

        if X.shape[0] > 50000:
            continue

        df = X.copy()

        df[target] = y

        meta = analyze_dataset(
            df,
            target
        )

        # Keep only numeric columns
        X_num = X.select_dtypes(
            include=["int64", "float64"]
        )

        if X_num.shape[1] == 0:
            continue

        scores = benchmark_models(
            X_num,
            y
        )

        numeric_scores = {
            k: v
            for k, v in scores.items()
            if isinstance(v, float)
        }

        if len(numeric_scores) == 0:
            continue

        best_model = max(
            numeric_scores,
            key=numeric_scores.get
        )

        save_meta_features(
            meta,
            best_model
        )

        print(
            "Winner:",
            best_model
        )

    except Exception as e:
        print(f"Error processing {dataset_id}: {e}")

   