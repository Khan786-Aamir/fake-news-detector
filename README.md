# 🕵️‍♂️ FAKE NEWS HUNTER

A sophisticated fake news detection system built with Flask and Machine Learning.

## 🚀 Live Demo

- **GitHub Pages**: [https://khan786-aamir.github.io/fake-news-detector/](https://khan786-aamir.github.io/fake-news-detector/)
- **Full Flask App**: Deploy on Railway/Heroku for complete ML functionality

## 🎯 Features

✅ **Machine Learning Detection** - TF-IDF + Logistic Regression  
✅ **Modern UI/UX** - Professional gradient design  
✅ **Real-time Analysis** - Instant fake news detection  
✅ **Confidence Scores** - Shows prediction probability  
✅ **Mobile Responsive** - Works on all devices  
✅ **Hindi + English Support** - Bilingual interface  
✅ **Auto Training** - Creates model if not found  

## 🛠️ Tech Stack

- **Backend**: Flask, scikit-learn, pandas, joblib
- **Frontend**: HTML5, CSS3, JavaScript
- **ML Model**: TF-IDF Vectorizer + Logistic Regression
- **Deployment**: GitHub Pages + GitHub Actions

## 📁 Project Structure

```
fake_news_detector/
├── app.py                 # Main Flask application
├── train.py              # Model training script
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html       # Flask template
├── static/
│   ├── app.js           # JavaScript functionality
│   └── style.css        # CSS styling
├── docs/
│   └── index.html       # GitHub Pages version
├── .github/workflows/
│   └── deploy.yml       # GitHub Actions workflow
├── Procfile             # Heroku deployment
├── runtime.txt          # Python version
└── railway.json         # Railway deployment
```

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Khan786-Aamir/fake-news-detector.git
   cd fake-news-detector
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model**
   ```bash
   python train.py
   ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```

5. **Open browser**
   ```
   http://localhost:5000
   ```

### Deployment Options

#### 🌐 GitHub Pages (Static Version)
- Automatically deployed via GitHub Actions
- Uses keyword-based detection
- URL: `https://khan786-aamir.github.io/fake-news-detector/`

#### ☁️ Railway (Full ML Version)
1. Visit [railway.app](https://railway.app)
2. Connect GitHub repository
3. Deploy automatically

#### 🚀 Heroku (Full ML Version)
1. Create Heroku app
2. Connect GitHub repository  
3. Enable automatic deploys

## 🧠 How It Works

### Machine Learning Pipeline

1. **Data Preprocessing** - Text cleaning and normalization
2. **Feature Extraction** - TF-IDF vectorization (1-2 grams)
3. **Model Training** - Logistic Regression classifier
4. **Prediction** - Real-time inference with confidence scores

### Detection Logic

```python
# Training Pipeline
Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_df=0.9, min_df=1, ngram_range=(1,2))),
    ('clf', LogisticRegression(max_iter=1000))
])
```

## 📊 Model Performance

- **Accuracy**: ~85-90% (depends on training data)
- **Features**: TF-IDF vectors with 1-2 gram analysis
- **Fallback**: Keyword-based detection for static deployment

## 🔧 Configuration

### Environment Variables
- `PORT`: Server port (default: 5000)
- `DEBUG`: Debug mode (default: False in production)

### Files
- `fake.csv`: Fake news training data
- `real.csv`: Real news training data  
- `model.pkl`: Trained ML model

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## 📝 License

MIT License - feel free to use for educational and commercial purposes.

## 👨‍💻 Author

**Khan786-Aamir**
- GitHub: [@Khan786-Aamir](https://github.com/Khan786-Aamir)
- Project: [fake-news-detector](https://github.com/Khan786-Aamir/fake-news-detector)

---

## 🎯 Future Enhancements

- [ ] Deep Learning models (BERT, RoBERTa)
- [ ] Multi-language support
- [ ] News source verification
- [ ] Real-time news scraping
- [ ] User feedback system
- [ ] API endpoints
- [ ] Database integration

---

**⭐ If you found this project helpful, please give it a star!**
