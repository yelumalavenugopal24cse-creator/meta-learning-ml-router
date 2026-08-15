from router.openml_loader import (
    load_openml_dataset
)

X, y = load_openml_dataset(
    61
)

print(X.head())
print(y.head())