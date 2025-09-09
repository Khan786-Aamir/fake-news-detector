# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import os
import subprocess
import sys

MODEL_PATH = "model.pkl"
app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)  # allow requests from frontend if served separately

# Function to create sample data if CSV files don't exist
def create_sample_data():
    import pandas as pd
    
    # Create sample fake news data
    fake_data = {
        'text': [
            "Breaking: Scientists discover cure for aging using simple kitchen ingredient",
            "Government secretly controls weather to manipulate elections",
            "Local man becomes millionaire overnight using this one weird trick",
            "Study shows that drinking water is actually harmful to your health",
            "Aliens finally make contact, demand pizza delivery to space"
        ] * 200  # Repeat to have more data
    }
    
    # Create sample real news data  
    real_data = {
        'text': [
            "Stock market shows steady growth amid economic recovery efforts",
            "New infrastructure bill passed by congress aims to improve roads",
            "Local school district receives funding for technology upgrades",
            "Weather forecast predicts mild temperatures for the weekend",
            "University researchers publish findings on renewable energy efficiency"
        ] * 200  # Repeat to have more data
    }
    
    # Create DataFrames and save as CSV
    fake_df = pd.DataFrame(fake_data)
    real_df = pd.DataFrame(real_data)
    
    fake_df.to_csv('fake.csv', index=False)
    real_df.to_csv('real.csv', index=False)
    print("✅ Sample datasets created successfully!")

# Load or create model
def load_or_create_model():
    if os.path.exists(MODEL_PATH):
        print("📦 Loading existing model...")
        return joblib.load(MODEL_PATH)
    else:
        print("🔄 Model not found. Creating sample data and training model...")
        
        # Create sample data if CSV files don't exist
        if not os.path.exists('fake.csv') or not os.path.exists('real.csv'):
            create_sample_data()
        
        # Train model
        print("🚀 Training model...")
        result = subprocess.run([sys.executable, 'train.py'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Model trained successfully!")
            return joblib.load(MODEL_PATH)
        else:
            print(f"❌ Error training model: {result.stderr}")
            # Return a dummy model for basic functionality
            from sklearn.pipeline import Pipeline
            from sklearn.feature_extraction.text import TfidfVectorizer
            from sklearn.linear_model import LogisticRegression
            import pandas as pd
            
            # Create a basic model with minimal training
            pipeline = Pipeline([
                ('tfidf', TfidfVectorizer(max_features=100)),
                ('clf', LogisticRegression())
            ])
            
            # Minimal training data
            X = ['This is fake news', 'This is real news'] * 10
            y = [1, 0] * 10
            
            pipeline.fit(X, y)
            joblib.dump(pipeline, MODEL_PATH)
            return pipeline

model = load_or_create_model()

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
