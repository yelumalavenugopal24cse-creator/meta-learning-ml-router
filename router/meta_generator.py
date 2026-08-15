import pandas as pd

def save_meta_features(
    meta,
    best_model,
    filename="router_training_data.csv"
):

    row = {

        "Rows":
        meta["rows"],

        "Cols":
        meta["cols"],

        "Missing":
        meta["missing_percent"],

        "Numeric":
        meta["numeric"],

        "Categorical":
        meta["categorical"],

        "BestModel":
        best_model
    }

    try:

        df = pd.read_csv(
            filename
        )

        df = pd.concat(
            [
                df,
                pd.DataFrame([row])
            ],
            ignore_index=True
        )

    except:

        df = pd.DataFrame(
            [row]
        )

    df.to_csv(
        filename,
        index=False
    )

    print(
        "Saved Meta Features"
    )