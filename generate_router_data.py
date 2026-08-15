from sklearn.datasets import (
    load_iris,
    load_wine,
    load_breast_cancer
)

import pandas as pd

from router.analyzer import (
    analyze_dataset
)

from router.benchmark import (
    benchmark_models
)

from router.meta_generator import (
    save_meta_features
)

datasets = [

    ("iris", load_iris()),

    ("wine", load_wine()),

    ("breast_cancer",
     load_breast_cancer())
]

for name, data in datasets:

    print(
        f"\nProcessing {name}"
    )

    X = pd.DataFrame(
        data.data
    )

    y = pd.Series(
        data.target
    )

    df = X.copy()

    df["target"] = y

    meta = analyze_dataset(
        df,
        "target"
    )

    scores = benchmark_models(
        X,
        y
    )

    best_model = max(
        scores,
        key=scores.get
    )

    print(
        "Winner:",
        best_model
    )

    save_meta_features(
        meta,
        best_model
    )