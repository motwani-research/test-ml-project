import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Train a simple ML model
def train_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)
    joblib.dump(model, "iris_model.pkl")  # Save the model
    print("Model trained and saved as iris_model.pkl")

# Make a prediction
def make_prediction():
    model = joblib.load("iris_model.pkl")  # Load the saved model
    sample = [[5.1, 3.5, 1.4, 0.2]]  # Example input
    prediction = model.predict(sample)
    print(f"Prediction for {sample}: {prediction}")

if __name__ == "__main__":
    train_model()  # Train the model
    make_prediction()  # Make a prediction
