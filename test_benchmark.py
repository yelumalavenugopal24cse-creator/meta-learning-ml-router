from sklearn.datasets import load_iris

from router.benchmark import benchmark_models

iris = load_iris()

X = iris.data
y = iris.target

results = benchmark_models(
    X,
    y
)

print(results)