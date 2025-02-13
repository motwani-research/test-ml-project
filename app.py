from flask import Flask, request, jsonify
from flask_cors import CORS
import model  # Import model.py

app = Flask(__name__)
CORS(app)

@app.route("/test", methods=["GET"])
def test_route():
    return jsonify({"message": "Testing successful...."})

@app.route("/train", methods=["POST"])
def train_route():
    model.train_model()
    return jsonify({"message": "Model trained successfully."})

@app.route("/predict", methods=["POST"])
def predict_route():
    try:
        data = request.get_json()
        sample = data.get("sample")
        if not sample or len(sample) != 4:
            return jsonify({"error": "Invalid input. Expected a list of 4 numerical values."}), 400
        
        prediction = model.make_prediction(sample)
        return jsonify({"prediction": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
