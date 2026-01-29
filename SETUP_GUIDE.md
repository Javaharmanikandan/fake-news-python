# AI Service Setup Guide

## Quick Setup

### Step 1: Install Python Dependencies

```bash
cd ai
pip install -r requirements.txt
```

**Note:** This will install:
- Flask (web framework)
- Transformers (ML models)
- PyTorch (deep learning)
- NLTK (natural language processing)
- TextStat (readability analysis)

**Installation time:** ~5-10 minutes (depends on internet speed)

### Step 2: Start the Service

```bash
python app.py
```

The service will:
1. Download ML models on first run (~250MB, one-time download)
2. Download NLTK data automatically
3. Start on `http://localhost:5000`

### Step 3: Verify Installation

Open another terminal and test:

```bash
curl http://localhost:5000/health
```

Expected response:
```json
{
  "status": "ok",
  "service": "advanced-fake-news-detection",
  "ml_models": "available"
}
```

## Troubleshooting

### Issue: "transformers not found"

**Solution:**
```bash
pip install transformers torch
```

### Issue: "NLTK data not found"

**Solution:** The script auto-downloads NLTK data. If it fails:
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('vader_lexicon'); nltk.download('stopwords')"
```

### Issue: Model download fails

**Solution:**
1. Check internet connection
2. The service will work with rule-based detection as fallback
3. Try again later - models download from HuggingFace

### Issue: Out of memory errors

**Solution:**
- The service uses CPU by default (no GPU required)
- If still having issues, reduce text length in requests
- Close other applications to free memory

### Issue: Port 5000 already in use

**Solution:** Change port in `app.py`:
```python
app.run(host='0.0.0.0', port=5001, debug=True)  # Change 5000 to 5001
```

And update backend `.env`:
```
AI_SERVICE_URL=http://localhost:5001
```

## Performance Tips

1. **First Request:** Takes 2-5 seconds (model loading)
2. **Subsequent Requests:** 0.5-2 seconds
3. **Model Caching:** Models stay in memory after first use

## Testing the Service

### Test with curl:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "text": "BREAKING: Scientists discover one weird trick to lose weight! Doctors hate this! Click here now!",
    "url": "https://example.com"
  }'
```

### Expected Response:

```json
{
  "result": "Fake",
  "confidence": 85.5,
  "explanation": "Found 3 suspicious keyword(s): one weird trick, doctors hate, click here. Writing patterns suggest unreliable content...",
  "source_credibility": "medium",
  "details": {
    "keyword_count": 3,
    "pattern_score": 45.0,
    "source_reliability": "medium",
    "sentiment": {...},
    "readability": {...},
    "ml_classification": {...},
    "final_score": 85.5
  }
}
```

## System Requirements

- **Python:** 3.8 or higher
- **RAM:** Minimum 2GB (4GB recommended)
- **Disk Space:** ~500MB for models and dependencies
- **Internet:** Required for first-time model download

## Optional: GPU Acceleration

If you have an NVIDIA GPU with CUDA:

1. Install CUDA-enabled PyTorch:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

2. Update `app.py` line with device:
```python
device=0  # Use GPU instead of -1 (CPU)
```

This will speed up predictions significantly.
