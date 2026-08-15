import pandas as pd

df = pd.read_csv(
    "datasets/iris.csv",
    skiprows=72,
    header=None,
    usecols=[1, 2, 3, 4, 5],
    names=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "species"
    ]
)

print(df.head())
print(df.shape)