from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


def benchmark_models(X, y):

    models = {
        "Logistic Regression":
        LogisticRegression(max_iter=1000),

        "Decision Tree":
        DecisionTreeClassifier(random_state=42),

        "Random Forest":
        RandomForestClassifier(random_state=42),

        "KNN":
        KNeighborsClassifier(),

        "SVM":
        SVC()
    }

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    scores = {}

    for name, model in models.items():

        try:

            model.fit(X_train, y_train)

            predictions = model.predict(X_test)

            accuracy = accuracy_score(
                y_test,
                predictions
            )

            scores[name] = round(
                accuracy,
                4
            )

        except Exception as e:

            scores[name] = str(e)

    return scores