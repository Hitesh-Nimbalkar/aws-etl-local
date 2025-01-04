import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

def train_ml_model():
    # Load a dataset (example using Iris dataset)
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize the RandomForestClassifier
    model = RandomForestClassifier()

    # Train the model
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    logging.info(f'Model accuracy: {accuracy:.4f}')
    return accuracy
