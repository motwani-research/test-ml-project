from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def test():
    return {"message": "Test function executed"}

@app.route("/test", methods=["GET"])
def test_route():
    return jsonify({"message": "Testing successful"})

@app.route("/model", methods=["POST"])
def model_route():
    data = request.get_json()
    print("Received payload:", data)
    return jsonify({"status": "success", "received": data})

@app.route("/predict", methods=["POST"])
def predict_route():
    result = test()
    return jsonify(result)

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)
