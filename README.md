This is the complete feature store that was built for [Feature Storage for ML with Feast: Part 1 – Building a Local Feature Store Infrastructure for Training and Prediction](https://kedion.medium.com/creating-a-feature-store-with-feast-part-1-37c380223e2f?source=user_profile---------0-------------------------------).

The feature store by itself is located in `breast_cancer`. The Jupyter notebook and Python scripts in the root directory of the repo are intended to help you prepare data, fetch features, train a model, and do inference.

Note that the data files in `breast_cancer/data` will very likely be outdated by the time you see this repository. After cloning the repo and before using the code, make sure to:

1. Run the Jupyter notebook `feast_data_preparation.ipynb` in the repo's root path to generate a toy dataset for the feature store.
2. Move the five generated files - `data_df1.parquet`, `data_df2.parquet`, `data_df3.parquet`, `data_df4.parquet`, and `target_df.parquet` - to `breast_cancer/data`.

Additionally, change the paths provided to to the class `FileSource` in `breast_cancer/definitions.py`

To find out more about how to use Feast, read [official Feast docs](https://docs.feast.dev/) and also [Feature Storage for ML with Feast: Part 1 – Building a Local Feature Store Infrastructure for Training and Prediction](https://kedion.medium.com/).
