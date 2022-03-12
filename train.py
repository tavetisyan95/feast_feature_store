# Importing dependencies
from feast import FeatureStore
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump

# Getting our FeatureStore
store = FeatureStore(repo_path="breast_cancer/")

# Retrieving the saved dataset and converting it to a DataFrame
training_df = store.get_saved_dataset(name="breast_cancer_dataset").to_df()

# Separating the features and labels
labels = training_df['target']
features = training_df.drop(
    labels=['target', 'event_timestamp', "patient_id"], 
    axis=1)

# Splitting the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(features, 
                                                    labels, 
                                                    stratify=labels)

# Creating and training LogisticRegression
reg = LogisticRegression()
reg.fit(X=X_train[sorted(X_train)], y=y_train)

# Saving the model
dump(value=reg, filename="model.joblib")