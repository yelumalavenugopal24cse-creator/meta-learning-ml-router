import openml

def load_openml_dataset(dataset_id):

    dataset = openml.datasets.get_dataset(
        dataset_id
    )

    X, y, _, _ = dataset.get_data(
        target=dataset.default_target_attribute
    )

    return X, y