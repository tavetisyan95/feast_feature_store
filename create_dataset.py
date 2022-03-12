# Importing dependencies
import pandas as pd
from feast import FeatureStore
from feast.infra.offline_stores.file_source import SavedDatasetFileStorage

# Getting our FeatureStore
store = FeatureStore(repo_path="breast_cancer/")

# Reading our targets as an entity DataFrame
entity_df = pd.read_parquet(path="breast_cancer/data/target_df.parquet")    

# Getting the indicated historical features
# and joining them with our entity DataFrame
training_data = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "df1_feature_view:mean radius",
        "df1_feature_view:mean texture",
        "df1_feature_view:mean perimeter",
        "df1_feature_view:mean area",
        "df1_feature_view:mean smoothness",
        "df2_feature_view:mean compactness",
        "df2_feature_view:mean concavity",
        "df2_feature_view:mean concave points",
        "df2_feature_view:mean symmetry",
        "df2_feature_view:mean fractal dimension",
        "df3_feature_view:radius error",
        "df3_feature_view:texture error",
        "df3_feature_view:perimeter error",
        "df3_feature_view:area error",
        "df3_feature_view:smoothness error",
        "df3_feature_view:compactness error",
        "df3_feature_view:concavity error",
        "df4_feature_view:concave points error",
        "df4_feature_view:symmetry error",
        "df4_feature_view:fractal dimension error",
        "df4_feature_view:worst radius",
        "df4_feature_view:worst texture",
        "df4_feature_view:worst perimeter",
        "df4_feature_view:worst area",
        "df4_feature_view:worst smoothness",
        "df4_feature_view:worst compactness",
        "df4_feature_view:worst concavity",
        "df4_feature_view:worst concave points",
        "df4_feature_view:worst symmetry",
        "df4_feature_view:worst fractal dimension"
    ]
)

# Storing the dataset as a local file
dataset = store.create_saved_dataset(
    from_=training_data,
    name="breast_cancer_dataset",
    storage=SavedDatasetFileStorage("breast_cancer/data/breast_cancer_dataset.parquet")
)