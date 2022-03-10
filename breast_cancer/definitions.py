# Importing dependencies
from google.protobuf.duration_pb2 import Duration
from feast import Entity, Feature, FeatureView, FileSource, ValueType

# Declaring an entity for the dataset
patient = Entity(name="patient_id", value_type=ValueType.INT64, description="The ID of the patient")

# Declaring the source of the first set of features
f_source1 = FileSource(
    path=r"C:\feast\breast_cancer\data\data_df1.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
df1_fv = FeatureView(
    name="df1_feature_view",
    ttl=Duration(seconds=86400 * 2),
    entities=["patient_id"],
    features=[
        Feature(name="mean radius", dtype=ValueType.FLOAT),
        Feature(name="mean texture", dtype=ValueType.FLOAT),
        Feature(name="mean perimeter", dtype=ValueType.FLOAT),
        Feature(name="mean area", dtype=ValueType.FLOAT),
        Feature(name="mean smoothness", dtype=ValueType.FLOAT)
        ],    
    batch_source=f_source1
)

# Declaring the source of the second set of features
f_source2 = FileSource(
    path=r"C:\feast\breast_cancer\data\data_df2.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the second set of features
df2_fv = FeatureView(
    name="df2_feature_view",
    ttl=Duration(seconds=86400 * 2),
    entities=["patient_id"],
    features=[
        Feature(name="mean compactness", dtype=ValueType.FLOAT),
        Feature(name="mean concavity", dtype=ValueType.FLOAT),
        Feature(name="mean concave points", dtype=ValueType.FLOAT),
        Feature(name="mean symmetry", dtype=ValueType.FLOAT),
        Feature(name="mean fractal dimension", dtype=ValueType.FLOAT)
        ],    
    batch_source=f_source2
)

# Declaring the source of the third set of features
f_source3 = FileSource(
    path=r"C:\feast\breast_cancer\data\data_df3.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the third set of features
df3_fv = FeatureView(
    name="df3_feature_view",
    ttl=Duration(seconds=86400 * 2),
    entities=["patient_id"],
    features=[
        Feature(name="radius error", dtype=ValueType.FLOAT),
        Feature(name="texture error", dtype=ValueType.FLOAT),
        Feature(name="perimeter error", dtype=ValueType.FLOAT),
        Feature(name="area error", dtype=ValueType.FLOAT),
        Feature(name="smoothness error", dtype=ValueType.FLOAT),
        Feature(name="compactness error", dtype=ValueType.FLOAT),
        Feature(name="concavity error", dtype=ValueType.FLOAT)
        ],    
    batch_source=f_source3
)

# Declaring the source of the fourth set of features
f_source4 = FileSource(
    path=r"C:\feast\breast_cancer\data\data_df4.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the fourth set of features
df4_fv = FeatureView(
    name="df4_feature_view",
    ttl=Duration(seconds=86400 * 2),
    entities=["patient_id"],
    features=[
        Feature(name="concave points error", dtype=ValueType.FLOAT),
        Feature(name="symmetry error", dtype=ValueType.FLOAT),
        Feature(name="fractal dimension error", dtype=ValueType.FLOAT),
        Feature(name="worst radius", dtype=ValueType.FLOAT),
        Feature(name="worst texture", dtype=ValueType.FLOAT),
        Feature(name="worst perimeter", dtype=ValueType.FLOAT),
        Feature(name="worst area", dtype=ValueType.FLOAT),
        Feature(name="worst smoothness", dtype=ValueType.FLOAT),
        Feature(name="worst compactness", dtype=ValueType.FLOAT),
        Feature(name="worst concavity", dtype=ValueType.FLOAT),
        Feature(name="worst concave points", dtype=ValueType.FLOAT),
        Feature(name="worst symmetry", dtype=ValueType.FLOAT),
        Feature(name="worst fractal dimension", dtype=ValueType.FLOAT),        
        ],    
    batch_source=f_source4
)

# Declaring the source of the targets
target_source = FileSource(
    path=r"C:\feast\breast_cancer\data\target_df.parquet", 
    created_timestamp_column="event_timestamp"
)

# Defining the targets
target_fv = FeatureView(
    name="target_feature_view",
    entities=["patient_id"],
    ttl=Duration(seconds=86400 * 2),
    features=[
        Feature(name="target", dtype=ValueType.INT32)        
        ],    
    batch_source=target_source
)