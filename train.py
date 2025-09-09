# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

# File paths (root folder se direct read karega)
FAKE_CSV = "fake.csv"
REAL_CSV = "real.csv"
MODEL_OUT = "model.pkl"

# Load data with error handling
try:
    fake = pd.read_csv(FAKE_CSV)[['text']].dropna().copy()
    real = pd.read_csv(REAL_CSV)[['text']].dropna().copy()
    print(f"✅ Loaded {len(fake)} fake news and {len(real)} real news articles")
except FileNotFoundError as e:
    print(f"❌ CSV file not found: {e}")
    print("📝 Using sample data for training...")
    
    # Create sample data
    fake_texts = [
        "Breaking: Scientists discover cure for aging using simple kitchen ingredient",
        "Government secretly controls weather to manipulate elections", 
        "Local man becomes millionaire overnight using this one weird trick",
        "Study shows that drinking water is actually harmful to your health",
        "Aliens finally make contact, demand pizza delivery to space",
        "Miracle diet pill makes you lose 50 pounds in one week",
        "Secret government facility discovered in your backyard"
    ] * 100
    
    real_texts = [
        "Stock market shows steady growth amid economic recovery efforts",
        "New infrastructure bill passed by congress aims to improve roads",
        "Local school district receives funding for technology upgrades", 
        "Weather forecast predicts mild temperatures for the weekend",
        "University researchers publish findings on renewable energy efficiency",
        "City council approves new park development project",
        "Local business receives award for community service"
    ] * 100
    
    fake = pd.DataFrame({'text': fake_texts})
    real = pd.DataFrame({'text': real_texts})
fake['label'] = 1   # 1 = Fake
real['label'] = 0   # 0 = Real

# Combine datasets
data = pd.concat([fake, real], ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)
X = data['text'].astype(str)
y = data['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.15, stratify=y, random_state=42
)

# Pipeline: TF-IDF + Logistic Regression
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words='english', max_df=0.9, min_df=1, ngram_range=(1,2))),
    ("clf", LogisticRegression(max_iter=1000))
])

print("Training model...")
pipeline.fit(X_train, y_train)

print("Evaluating on test set...")
y_pred = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model pipeline
joblib.dump(pipeline, MODEL_OUT)
print(f"✅ Saved model to {MODEL_OUT}")
