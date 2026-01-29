# Advanced Fake News Detection AI Service

This service provides comprehensive fake news detection using multiple techniques:

## Features

### 1. **Machine Learning Model**
- Uses DistilBERT transformer model for text classification
- Analyzes semantic content and context
- Provides confidence scores based on learned patterns

### 2. **Advanced NLP Analysis**
- **Sentiment Analysis**: Detects emotional manipulation and extreme sentiment
- **Readability Analysis**: Identifies poor writing quality (common in fake news)
- **Linguistic Pattern Detection**: Analyzes capitalization, punctuation, repetition

### 3. **Expanded Keyword Database**
- 50+ suspicious keywords and phrases
- Covers financial scams, health scams, clickbait, conspiracy theories
- Pattern matching for common fake news indicators

### 4. **Source Reliability Checking**
- Expanded list of trusted news sources (20+ major outlets)
- Domain pattern analysis
- URL credibility assessment

### 5. **Fact-Checking Integration**
- Identifies fact-checkable claims
- Flags content requiring verification
- Ready for integration with fact-checking APIs

### 6. **Semantic Similarity Checking**
- Compares against known fake news patterns
- Detects similar content to previously identified fake news

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Create virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

**Note:** The first time you run the service, it will download the ML models (~250MB). This happens automatically on first use.

### Alternative: Lightweight Installation

If you want to skip ML models (uses rule-based detection only):
```bash
pip install Flask==3.0.0 flask-cors==4.0.0 requests==2.31.0
```

## Usage

### Start the Service

```bash
python app.py
```

The service will run on `http://localhost:5000`

### API Endpoints

#### Health Check
```bash
GET /health
```

Response:
```json
{
  "status": "ok",
  "service": "advanced-fake-news-detection",
  "ml_models": "available"
}
```

#### Prediction
```bash
POST /predict
Content-Type: application/json

{
  "text": "Your news article text here...",
  "url": "https://example.com/article"  // optional
}
```

Response:
```json
{
  "result": "Fake",
  "confidence": 85.5,
  "explanation": "Found 3 suspicious keyword(s): free money, guaranteed, act now. Writing patterns suggest unreliable content. Excessive capitalization detected.",
  "source_credibility": "medium",
  "details": {
    "keyword_count": 3,
    "pattern_score": 45.0,
    "source_reliability": "medium",
    "sentiment": {"compound": -0.8, "pos": 0.1, "neu": 0.2, "neg": 0.7},
    "readability": {"flesch_score": 35.2, "fk_grade": 12.5, "suspicion_score": 15},
    "ml_classification": {"label": "NEGATIVE", "score": 0.92},
    "fact_check": {"checked": true, "verdict": "needs_verification"},
    "similarity_check": {"similar": false, "matches": []},
    "final_score": 85.5
  }
}
```

## How It Works

The detection system uses a **multi-factor scoring approach**:

1. **Keyword Analysis** (0-25 points): Matches suspicious phrases
2. **Linguistic Patterns** (0-25 points): Analyzes writing quality
3. **Source Reliability** (0-20 points): Checks domain credibility
4. **Sentiment Analysis** (0-10 points): Detects emotional manipulation
5. **Readability** (0-10 points): Identifies poor writing
6. **ML Classification** (0-15 points): Transformer model analysis
7. **Fact-Checking** (0-10 points): Flags verifiable claims
8. **Similarity Check** (0-15 points): Matches known fake patterns

**Total Score Calculation:**
- **Score ≥ 65**: Classified as "Fake"
- **Score ≤ 25**: Classified as "Real"
- **25 < Score < 65**: Classified as "Doubtful"

## Performance

- **First Request**: ~2-5 seconds (model loading)
- **Subsequent Requests**: ~0.5-2 seconds (depending on text length)
- **Model Size**: ~250MB (downloaded automatically)

## Troubleshooting

### Model Download Issues
If models fail to download:
1. Check internet connection
2. The service will fall back to rule-based detection
3. Manually download models using:
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
```

### NLTK Data Issues
If you see NLTK data errors, the script will automatically download required data. If it fails:
```python
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')
```

### Memory Issues
If you encounter memory errors:
- Use CPU mode (default): `device=-1`
- Reduce text length before sending
- Consider using a smaller model

## Future Enhancements

- Integration with Google Fact Check API
- Real-time fact-checking against multiple sources
- Image analysis for fake images
- Multi-language support
- Custom model training on fake news datasets
- Database of known fake news for similarity matching

## License

This is a college project for educational purposes.
