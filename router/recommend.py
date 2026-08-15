import joblib
import pandas as pd


def recommend_algorithms(
    rows,
    cols,
    missing,
    numeric,
    categorical
):

    model = joblib.load(
        "models/router.pkl"
    )

    encoder = joblib.load(
        "models/label_encoder.pkl"
    )

    sample = pd.DataFrame(
        [
            {
                "Rows": rows,
                "Cols": cols,
                "Missing": missing,
                "Numeric": numeric,
                "Categorical": categorical
            }
        ]
    )

    probs = model.predict_proba(
        sample
    )[0]

    classes = encoder.inverse_transform(
        range(len(probs))
    )

    ranking = list(
        zip(classes, probs)
    )

    ranking.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return ranking[:3]