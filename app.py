# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import os

MODEL_PATH = "model.pkl"
app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)  # allow requests from frontend if served separately

# Load model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found. Run `python train.py` to create {MODEL_PATH}")
model = joblib.load(MODEL_PATH)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400
    text = data["text"]
    pred = int(model.predict([text])[0])
    prob = None
    if hasattr(model, "predict_proba"):
        prob = float(model.predict_proba([text])[0][pred])
    return jsonify({"label": pred, "probability": prob})

if __name__ == "__main__":
    app.run(debug=True)  # set debug=False in production
