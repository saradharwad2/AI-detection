from src.visualize import plot_sensor_trends
from src.data_loader import load_data
from src.preprocess import preprocess
from src.train_model import train_model
from src.predict import predict

from src.visualize import plot_confusion_matrix
from src.visualize import plot_failure_distribution
from src.visualize import plot_correlation_heatmap
from src.visualize import plot_feature_importance

from sklearn.metrics import accuracy_score, classification_report


# Load dataset
data = load_data("data/predictive_maintenance.csv")

data = load_data("data/predictive_maintenance.csv")

plot_failure_distribution(data)
plot_correlation_heatmap(data)
plot_sensor_trends(data)

# Generate EDA graphs
plot_failure_distribution(data)
plot_correlation_heatmap(data)

# Preprocess data
X_train, X_test, y_train, y_test = preprocess(data)

# Train model
model = train_model(X_train, y_train)

# Predict
preds = predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, preds)
print("Model Accuracy:", accuracy)

# Classification report
print(classification_report(y_test, preds))

# Confusion matrix
plot_confusion_matrix(y_test, preds)

# Feature importance
feature_names = data.drop(
    ["UDI","Product ID","Type","Machine failure","TWF","HDF","PWF","OSF","RNF"],
    axis=1
).columns

plot_feature_importance(model, feature_names)