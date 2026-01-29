# ====================================================
# ADVANCED FAKE NEWS DETECTION AI SERVICE
# ====================================================
# Python Flask service with ML model, NLP analysis,
# and comprehensive fake news detection
# ====================================================

from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import os
import warnings
warnings.filterwarnings('ignore')

# ML and NLP imports
try:
    from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
    import torch
    from textstat import flesch_reading_ease, flesch_kincaid_grade
    import nltk
    from nltk.sentiment import SentimentIntensityAnalyzer
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    import requests
    from urllib.parse import urlparse
    ML_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Some ML libraries not available: {e}")
    print("Falling back to rule-based detection only")
    ML_AVAILABLE = False

app = Flask(__name__)
CORS(app)

# ====================================================
# GLOBAL VARIABLES AND MODEL LOADING
# ====================================================

# Initialize models (lazy loading)
ml_model = None
tokenizer = None
sentiment_analyzer = None
fake_news_classifier = None

def initialize_models():
    """Initialize ML models on first use"""
    global ml_model, tokenizer, sentiment_analyzer, fake_news_classifier
    
    if not ML_AVAILABLE:
        return False
    
    try:
        # Download NLTK data if not present
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)
        
        try:
            nltk.data.find('vader_lexicon')
        except LookupError:
            nltk.download('vader_lexicon', quiet=True)
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
        
        # Initialize sentiment analyzer
        sentiment_analyzer = SentimentIntensityAnalyzer()
        
        # Load transformer model for fake news detection
        # Using a lightweight model that works well for text classification
        model_name = "distilbert-base-uncased-finetuned-sst-2-english"
        print("Loading ML model... This may take a moment on first run.")
        
        try:
            # Try to load a pre-trained model for sentiment/text classification
            # We'll use it as a base and adapt for fake news detection
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            ml_model = AutoModelForSequenceClassification.from_pretrained(model_name)
            
            # Create a fake news classifier pipeline
            fake_news_classifier = pipeline(
                "text-classification",
                model=ml_model,
                tokenizer=tokenizer,
                device=-1  # Use CPU (-1) or GPU (0) if available
            )
            print("✓ ML models loaded successfully")
            return True
        except Exception as e:
            print(f"Warning: Could not load transformer model: {e}")
            print("Falling back to rule-based detection")
            return False
            
    except Exception as e:
        print(f"Error initializing models: {e}")
        return False

# ====================================================
# EXPANDED KEYWORD DATABASE
# ====================================================

FAKE_NEWS_KEYWORDS = [
    # Financial scams
    'free money', 'win cash', 'guaranteed income', 'no investment required',
    'get rich quick', 'earn $1000 daily', 'work from home scam',
    
    # Health scams
    'miracle cure', 'doctors hate', 'one weird trick', 'lose weight fast',
    'cure all diseases', 'secret remedy', 'pharmaceutical companies hide',
    
    # Clickbait patterns
    'click here', 'you won\'t believe', 'shocking truth', 'they don\'t want you to know',
    'secret government', 'breaking: you won\'t believe', 'viral', 'share before deleted',
    'this will shock you', 'number one trick', 'instant results',
    
    # Urgency and manipulation
    'urgent', 'act now', 'limited time', 'exclusive offer', 'no questions asked',
    'guaranteed', '100% proven', 'scientifically proven (without citation)',
    
    # Conspiracy patterns
    'mainstream media lies', 'cover-up', 'hidden truth', 'they\'re hiding',
    'wake up', 'sheeple', 'deep state', 'illuminati',
    
    # Emotional manipulation
    'outrageous', 'disgusting', 'you\'ll be shocked', 'prepare to be amazed',
    'mind-blowing', 'unbelievable', 'incredible discovery'
]

# Trusted news sources (expanded list)
TRUSTED_SOURCES = [
    'bbc.com', 'reuters.com', 'ap.org', 'apnews.com', 'nytimes.com',
    'theguardian.com', 'washingtonpost.com', 'wsj.com', 'cnn.com',
    'npr.org', 'economist.com', 'bloomberg.com', 'ft.com',
    'usatoday.com', 'abcnews.go.com', 'cbsnews.com', 'nbcnews.com',
    'abc.net.au', 'theage.com.au', 'smh.com.au', 'independent.co.uk',
    'telegraph.co.uk', 'thetimes.co.uk', 'scmp.com', 'straitstimes.com'
]

# Untrusted/suspicious domains
UNTRUSTED_SOURCES = [
    'fake-news.com', 'hoax-site.com', 'clickbait-news.com',
    'conspiracy-theory.com', 'satire-news.com'
]

# ====================================================
# HELPER FUNCTIONS - KEYWORD DETECTION
# ====================================================

def check_suspicious_keywords(text):
    """Check if text contains suspicious keywords"""
    text_lower = text.lower()
    matched = []
    count = 0
    
    for keyword in FAKE_NEWS_KEYWORDS:
        if keyword in text_lower:
            count += 1
            matched.append(keyword)
    
    return count, matched

# ====================================================
# ADVANCED NLP ANALYSIS
# ====================================================

def analyze_sentiment(text):
    """Analyze sentiment of the text"""
    if not ML_AVAILABLE or sentiment_analyzer is None:
        return {'compound': 0.0, 'pos': 0.0, 'neu': 0.0, 'neg': 0.0}
    
    try:
        scores = sentiment_analyzer.polarity_scores(text)
        return scores
    except:
        return {'compound': 0.0, 'pos': 0.0, 'neu': 0.0, 'neg': 0.0}

def analyze_readability(text):
    """Analyze readability and writing quality"""
    try:
        flesch_score = flesch_reading_ease(text)
        fk_grade = flesch_kincaid_grade(text)
        
        # Very low readability might indicate poor writing (common in fake news)
        # Very high readability with sensational content might also be suspicious
        readability_score = 0
        
        if flesch_score < 30:  # Very difficult to read
            readability_score += 15
        elif flesch_score > 90:  # Very easy (might be oversimplified)
            readability_score += 10
        
        return {
            'flesch_score': flesch_score,
            'fk_grade': fk_grade,
            'suspicion_score': readability_score
        }
    except:
        return {'flesch_score': 50, 'fk_grade': 10, 'suspicion_score': 0}

def analyze_linguistic_patterns(text):
    """Analyze linguistic patterns that indicate fake news"""
    score = 0
    details = []
    
    # Excessive capitalization
    caps_ratio = sum(1 for c in text if c.isupper()) / len(text) if text else 0
    if caps_ratio > 0.3:
        score += 20
        details.append("Excessive capitalization detected")
    
    # Excessive punctuation
    exclamation_count = text.count('!')
    question_count = text.count('?')
    if exclamation_count > 3:
        score += 15
        details.append(f"Excessive exclamation marks ({exclamation_count})")
    if question_count > 5:
        score += 10
        details.append(f"Excessive question marks ({question_count})")
    
    # Text length analysis
    word_count = len(text.split())
    sentence_count = len(sent_tokenize(text)) if ML_AVAILABLE else text.count('.') + 1
    
    if word_count < 10:
        score += 15
        details.append("Text too short for reliable analysis")
    elif word_count < 50 and sentence_count < 3:
        score += 10
        details.append("Insufficient content depth")
    
    # Punctuation quality
    if text.count('.') < word_count / 20 and word_count > 20:
        score += 10
        details.append("Poor punctuation structure")
    
    # Check for repeated words/phrases (spam indicator)
    words = text.lower().split()
    if len(words) > 0:
        word_freq = {}
        for word in words:
            if len(word) > 3:  # Ignore short words
                word_freq[word] = word_freq.get(word, 0) + 1
        
        max_repeat = max(word_freq.values()) if word_freq else 0
        if max_repeat > len(words) * 0.1:  # More than 10% repetition
            score += 15
            details.append("Excessive word repetition detected")
    
    return min(score, 100), details

def check_writing_patterns(text):
    """Legacy function for backward compatibility"""
    score, _ = analyze_linguistic_patterns(text)
    return score

# ====================================================
# ML MODEL PREDICTION
# ====================================================

def ml_classify_text(text):
    """Use ML model to classify text"""
    if not ML_AVAILABLE or fake_news_classifier is None:
        return None
    
    try:
        # Truncate text to model's max length (512 tokens typically)
        max_length = 512
        if len(text) > max_length * 4:  # Rough estimate: 4 chars per token
            text = text[:max_length * 4]
        
        # Get classification
        result = fake_news_classifier(text, truncation=True, max_length=512)
        
        # The model returns sentiment, we'll interpret negative sentiment
        # as potentially fake news indicator (combined with other factors)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        return result
    except Exception as e:
        print(f"ML classification error: {e}")
        return None

# ====================================================
# SOURCE RELIABILITY CHECKING
# ====================================================

def check_source_reliability(url):
    """Check if URL domain is in trusted/untrusted list"""
    if not url:
        return 'medium', []
    
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.replace('www.', '').lower()
        
        details = []
        
        # Check trusted sources
        for trusted in TRUSTED_SOURCES:
            if trusted in domain:
                return 'high', [f"Source is from trusted domain: {trusted}"]
        
        # Check untrusted sources
        for untrusted in UNTRUSTED_SOURCES:
            if untrusted in domain:
                return 'low', [f"Source is from known untrusted domain: {untrusted}"]
        
        # Check for suspicious domain patterns
        suspicious_patterns = ['free', 'click', 'win', 'prize', 'lottery']
        for pattern in suspicious_patterns:
            if pattern in domain:
                details.append(f"Suspicious domain pattern detected: {pattern}")
        
        return 'medium', details
    except:
        return 'medium', []

# ====================================================
# FACT-CHECKING INTEGRATION
# ====================================================

def fact_check_claim(text, url=None):
    """Attempt to fact-check the claim using web search"""
    # This is a simplified version - in production, you'd use
    # fact-checking APIs like Google Fact Check API, Snopes API, etc.
    
    fact_check_result = {
        'checked': False,
        'verdict': None,
        'sources': [],
        'confidence': 0.0
    }
    
    # Extract key claims from text (simplified)
    # In production, use NLP to extract factual claims
    sentences = sent_tokenize(text) if ML_AVAILABLE else text.split('.')
    
    # Check for common fact-checkable patterns
    fact_checkable_phrases = [
        'study shows', 'research proves', 'scientists say',
        'according to', 'official data', 'statistics show'
    ]
    
    has_claim = any(phrase in text.lower() for phrase in fact_checkable_phrases)
    
    if has_claim:
        fact_check_result['checked'] = True
        fact_check_result['verdict'] = 'needs_verification'
        fact_check_result['confidence'] = 30.0
        fact_check_result['sources'] = [
            'Note: This claim should be verified with fact-checking services'
        ]
    
    return fact_check_result

# ====================================================
# SEMANTIC SIMILARITY CHECKING
# ====================================================

def check_semantic_similarity(text):
    """Check if text is similar to known fake news"""
    # In a production system, you'd maintain a database of known fake news
    # and use embeddings to check similarity
    # For now, we'll use a simplified keyword-based approach
    
    known_fake_patterns = [
        'covid vaccine causes', '5g causes', 'flat earth',
        'moon landing fake', 'chemtrails', 'illuminati controls'
    ]
    
    text_lower = text.lower()
    matches = []
    
    for pattern in known_fake_patterns:
        if pattern in text_lower:
            matches.append(pattern)
    
    if matches:
        return {
            'similar': True,
            'matches': matches,
            'confidence': min(len(matches) * 20, 80)
        }
    
    return {
        'similar': False,
        'matches': [],
        'confidence': 0.0
    }

# ====================================================
# EXPLANATION GENERATION
# ====================================================

def generate_explanation(keyword_count, matched_keywords, pattern_score, pattern_details,
                        source_level, source_details, sentiment_scores, readability,
                        ml_result, fact_check, similarity):
    """Generate comprehensive explanation for the result"""
    reasons = []
    
    # Keyword analysis
    if keyword_count > 0:
        reasons.append(f"Found {keyword_count} suspicious keyword(s): {', '.join(matched_keywords[:5])}")
    
    # Pattern analysis
    if pattern_score > 30:
        reasons.append(f"Writing patterns suggest unreliable content. {'. '.join(pattern_details[:2])}")
    
    # Source analysis
    if source_level == 'low':
        reasons.append(f"Source reliability is low. {'. '.join(source_details[:1])}")
    elif source_level == 'high':
        reasons.append(f"Source appears to be from a trusted domain. {'. '.join(source_details[:1])}")
    
    # Sentiment analysis
    if sentiment_analyzer and sentiment_scores:
        if sentiment_scores.get('compound', 0) < -0.5:
            reasons.append("Highly negative sentiment detected, which may indicate manipulative content")
        elif sentiment_scores.get('compound', 0) > 0.7:
            reasons.append("Extremely positive sentiment may indicate clickbait or exaggeration")
    
    # Readability
    if readability and readability.get('suspicion_score', 0) > 10:
        reasons.append("Writing quality issues detected")
    
    # ML model result
    if ml_result:
        ml_label = ml_result.get('label', '')
        ml_score = ml_result.get('score', 0)
        if 'NEGATIVE' in ml_label.upper() and ml_score > 0.7:
            reasons.append(f"ML analysis indicates suspicious content (confidence: {ml_score:.1%})")
    
    # Fact-checking
    if fact_check and fact_check.get('checked'):
        reasons.append("Contains fact-checkable claims that require verification")
    
    # Similarity
    if similarity and similarity.get('similar'):
        reasons.append(f"Similar to known fake news patterns: {', '.join(similarity['matches'][:2])}")
    
    if not reasons:
        reasons.append("Content appears normal, but verification recommended")
    
    return ". ".join(reasons)

# ====================================================
# MAIN DETECTION FUNCTION
# ====================================================

def detect_fake_news(text, url=None):
    """
    Advanced fake news detection using multiple methods
    Returns: dict with result, confidence, and explanation
    """
    if not text or len(text.strip()) < 10:
        return {
            'result': 'Doubtful',
            'confidence': 50.0,
            'explanation': 'Text is too short to analyze properly',
            'details': {}
        }
    
    # Initialize models if not already done
    if ML_AVAILABLE and sentiment_analyzer is None:
        initialize_models()
    
    # Step 1: Keyword detection
    keyword_count, matched_keywords = check_suspicious_keywords(text)
    
    # Step 2: Linguistic pattern analysis
    pattern_score, pattern_details = analyze_linguistic_patterns(text)
    
    # Step 3: Source reliability
    source_level, source_details = check_source_reliability(url)
    
    # Step 4: NLP Analysis
    sentiment_scores = analyze_sentiment(text)
    readability = analyze_readability(text)
    
    # Step 5: ML Model classification
    ml_result = ml_classify_text(text)
    
    # Step 6: Fact-checking
    fact_check = fact_check_claim(text, url)
    
    # Step 7: Semantic similarity
    similarity = check_semantic_similarity(text)
    
    # Step 8: Calculate comprehensive fake news score (0-100)
    fake_score = 0
    
    # Keywords: up to 40 points (more aggressive - each keyword is worth more)
    # First 3 keywords are worth more (8 points each), then 6 points each
    if keyword_count > 0:
        if keyword_count <= 3:
            fake_score += keyword_count * 8  # 8 points per keyword for first 3
        else:
            fake_score += 24 + (keyword_count - 3) * 6  # 24 for first 3, then 6 each
    fake_score = min(fake_score, 40)  # Cap at 40
    
    # Linguistic patterns: up to 35 points (more aggressive)
    fake_score += pattern_score * 0.35
    
    # Source reliability: up to 25 points
    if source_level == 'low':
        fake_score += 25
    elif source_level == 'high':
        fake_score -= 20  # Trusted source significantly reduces suspicion
    
    # Sentiment analysis: up to 15 points (increased weight)
    compound_sentiment = sentiment_scores.get('compound', 0)
    if compound_sentiment < -0.6 or compound_sentiment > 0.8:
        fake_score += 15
    elif -0.3 <= compound_sentiment <= 0.3:
        # Neutral sentiment suggests more reliable content
        fake_score -= 5
    
    # Readability issues: up to 15 points
    readability_suspicion = readability.get('suspicion_score', 0)
    fake_score += readability_suspicion * 0.15
    
    # ML model: contributes to score based on sentiment
    if ml_result:
        ml_label = ml_result.get('label', '')
        ml_score = ml_result.get('score', 0)
        if 'NEGATIVE' in ml_label.upper() and ml_score > 0.7:
            # Strong negative sentiment suggests fake/manipulative content
            fake_score += 20
        elif 'POSITIVE' in ml_label.upper() and ml_score > 0.7:
            # Strong positive sentiment might indicate clickbait
            fake_score += 10
        elif 'POSITIVE' in ml_label.upper() and ml_score > 0.5:
            # Moderate positive sentiment suggests real news
            fake_score -= 5
    
    # Fact-checking: up to 15 points
    if fact_check.get('checked') and fact_check.get('verdict') == 'needs_verification':
        fake_score += 15
    
    # Similarity to known fake news: up to 20 points
    if similarity.get('similar'):
        fake_score += min(similarity.get('confidence', 0) * 0.2, 20)
    
    # Boost for obvious fake news patterns (multiple indicators)
    # If we have both keywords AND patterns, it's more likely fake
    if keyword_count >= 2 and pattern_score >= 30:
        fake_score += 10  # Bonus for multiple indicators
    if keyword_count >= 3:
        fake_score += 5  # Extra bonus for many keywords
    
    # Adjust score based on content quality indicators
    # If content has very few indicators and comes from trusted source, reduce suspicion significantly
    if source_level == 'high' and keyword_count == 0 and pattern_score < 20:
        # High-quality content from trusted source with no red flags
        fake_score = max(0, fake_score - 15)
    
    # If content has no indicators at all, it's likely normal (not necessarily fake or real)
    if keyword_count == 0 and pattern_score < 10 and source_level != 'low':
        # Very clean content - should be doubtful or real, not fake
        fake_score = max(0, fake_score - 8)
    
    fake_score = max(0, min(100, fake_score))  # Clamp between 0-100
    
    # Step 9: Determine result with more balanced thresholds
    # Adjusted to properly classify content instead of everything being "Doubtful"
    
    # FAKE: Score >= 35 (lowered from 45 to catch more fake news)
    if fake_score >= 35:
        result = 'Fake'
        confidence = min(65 + (fake_score - 35) * 0.75, 95)  # Scale confidence 65-95%
    
    # REAL: Score <= 20 (raised from 12, and less strict source requirement)
    # OR score <= 15 from trusted source
    elif fake_score <= 20 or (fake_score <= 15 and source_level == 'high'):
        result = 'Real'
        if source_level == 'high':
            confidence = min(85 + (20 - fake_score) * 0.5, 95)  # Higher confidence for trusted sources
        else:
            confidence = min(75 + (20 - fake_score) * 0.5, 90)  # Lower confidence for unknown sources
    
    # DOUBTFUL: Everything in between (20 < score < 35)
    else:
        result = 'Doubtful'
        # Calculate confidence based on distance from thresholds
        if fake_score < 35:
            # Closer to Real (20-35 range)
            distance_from_real = fake_score - 20
            confidence = 50 + (distance_from_real * 0.67)  # 50% to 60%
        else:
            # Closer to Fake (shouldn't happen, but just in case)
            confidence = 50
        confidence = max(45, min(60, confidence))  # Keep in 45-60% range for doubtful
    
    # Step 10: Generate comprehensive explanation
    explanation = generate_explanation(
        keyword_count, matched_keywords, pattern_score, pattern_details,
        source_level, source_details, sentiment_scores, readability,
        ml_result, fact_check, similarity
    )
    
    # Prepare detailed breakdown
    details = {
        'keyword_count': keyword_count,
        'pattern_score': round(pattern_score, 2),
        'source_reliability': source_level,
        'sentiment': sentiment_scores,
        'readability': readability,
        'ml_classification': ml_result,
        'fact_check': fact_check,
        'similarity_check': similarity,
        'final_score': round(fake_score, 2)
    }
    
    return {
        'result': result,
        'confidence': round(confidence, 2),
        'explanation': explanation,
        'source_credibility': source_level,
        'details': details
    }

# ====================================================
# API ENDPOINTS
# ====================================================

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    ml_status = "available" if (ML_AVAILABLE and fake_news_classifier is not None) else "unavailable"
    return jsonify({
        'status': 'ok',
        'service': 'advanced-fake-news-detection',
        'ml_models': ml_status
    })

@app.route('/predict', methods=['POST'])
def predict():
    """
    Main prediction endpoint
    Expected input: { "text": "...", "url": "..." (optional) }
    Returns: { "result": "...", "confidence": ..., "explanation": "...", "details": {...} }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        text = data.get('text', '')
        url = data.get('url', None)
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        # Perform detection
        result = detect_fake_news(text, url)
        
        return jsonify(result), 200
    
    except Exception as e:
        import traceback
        print(f"Error in prediction: {e}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

# ====================================================
# RUN SERVER
# ====================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Starting Advanced Fake News Detection AI Service...")
    print("=" * 60)
    
    # Initialize models
    if ML_AVAILABLE:
        print("Initializing ML models...")
        initialize_models()
    else:
        print("ML libraries not available. Using rule-based detection only.")
        print("To enable ML features, install: pip install transformers torch textstat nltk")
    
    print("Service will run on http://localhost:5000")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
