import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


df = pd.read_csv("router_training_data.csv")

X = df[
    [
        "Rows",
        "Cols",
        "Missing",
        "Numeric",
        "Categorical"
    ]
]

y = df["BestModel"]

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

router = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

router.fit(X_train, y_train)

predictions = router.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    f"Router Accuracy: {accuracy:.4f}"
)

joblib.dump(
    router,
    "models/router.pkl"
)

joblib.dump(
    encoder,
    "models/label_encoder.pkl"
)

print("Model Saved")