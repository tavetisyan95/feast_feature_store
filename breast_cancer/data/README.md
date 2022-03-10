Note that the data files here will very likely be outdated by the time you see this repository. After cloning the repo and before using the code, make sure to:

1. Run the Jupyter notebook `feast_data_preparation.ipynb` in the repo's root path to generate a toy dataset for the feature store.
2. Move the five generated files - `data_df1.parquet`, `data_df2.parquet`, `data_df3.parquet`, `data_df4.parquet`, and `target_df.parquet` - to `breast_cancer/data`.

To find out more about how to use Feast, read [official Feast docs](https://docs.feast.dev/) and also [Feature Storage for ML with Feast: Part 1 – Building a Local Feature Store Infrastructure for Training and Prediction](https://kedion.medium.com/).