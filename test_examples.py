"""
FAKE NEWS DETECTION - TEST EXAMPLES
Copy these examples and test them with the detection system
"""

# ====================================================
# FAKE NEWS EXAMPLES (Will show as FAKE)
# ====================================================

FAKE_NEWS_EXAMPLES = [
    {
        "category": "Financial Scam",
        "text": "URGENT! WIN CASH NOW! Guaranteed $1000 daily income with ZERO investment! This exclusive offer is available for LIMITED TIME ONLY! Act now! Free money waiting for you!",
        "url": "https://get-rich-quick.com",
        "expected": "FAKE",
        "confidence": "80-90%"
    },
    {
        "category": "Health Scam",
        "text": "BREAKING: ONE WEIRD TRICK doctors HATE! Click here for FREE access to the miraculous cure that pharmaceutical companies don't want you to know about! Lose 50 pounds in 3 days! This MIRACLE CURE has been BANNED BY DOCTORS! Limited time!",
        "url": "https://instant-weight-loss.com",
        "expected": "FAKE",
        "confidence": "85-95%"
    },
    {
        "category": "Health Scam #2",
        "text": "SHOCKING: Cure all diseases with this SECRET REMEDY! Doctors HATE this trick! Cancer cure hidden by pharmaceutical companies! Click here NOW for FREE information! Share before it gets deleted!",
        "url": "https://secret-health-cure.com",
        "expected": "FAKE",
        "confidence": "85-90%"
    },
    {
        "category": "Clickbait Conspiracy",
        "text": "You won't BELIEVE what happened! Shocking truth they don't want you to know! The mainstream media is LYING! Wake up, sheeple! This viral story will blow your mind! Share before deleted!",
        "url": "https://truth-revealed.com",
        "expected": "FAKE or DOUBTFUL",
        "confidence": "60-75%"
    },
    {
        "category": "Financial Scam #2",
        "text": "MAKE EASY CASH NOW! Work from home scam exposed - but wait, THIS METHOD WORKS! Guaranteed income! NO investment required! Click here for instant results! Free gift included!",
        "url": "https://work-from-home-money.com",
        "expected": "FAKE",
        "confidence": "75-85%"
    },
    {
        "category": "Conspiracy Theory",
        "text": "BREAKING: Deep state cover-up revealed! Mainstream media LIES! The government conspiracy is real! Hidden truth suppressed! Wake up! They're hiding the real story! This will shock you!",
        "url": "https://conspiracy-truth.com",
        "expected": "DOUBTFUL",
        "confidence": "55-70%"
    },
    {
        "category": "Sensational Clickbait",
        "text": "INCREDIBLE DISCOVERY! Scientists find mind-blowing breakthrough! You won't believe what they found! This stunning revelation will change everything! Click now! Prepare to be amazed!",
        "url": "https://viral-click.com",
        "expected": "DOUBTFUL",
        "confidence": "50-65%"
    },
]

# ====================================================
# REAL NEWS EXAMPLES (Will show as REAL)
# ====================================================

REAL_NEWS_EXAMPLES = [
    {
        "category": "Medical Research",
        "text": "According to a study published in the Journal of Medical Research, researchers found that regular exercise can significantly improve cardiovascular health. The study, which followed 10,000 participants over five years, showed a 20% reduction in heart disease risk among those who exercised regularly. The findings were reviewed by independent experts in the field.",
        "url": "https://www.bbc.com/health/research",
        "expected": "REAL",
        "confidence": "85-90%"
    },
    {
        "category": "Political News",
        "text": "The city council met yesterday to discuss and approve the new budget proposal. The $50 million environmental protection initiative received support from 256 lawmakers while 89 voted against it. Environmental groups praised the decision as a significant step toward reducing carbon emissions.",
        "url": "https://www.bbc.com/news",
        "expected": "REAL",
        "confidence": "88-92%"
    },
    {
        "category": "Technology News",
        "text": "Scientists at MIT announced a breakthrough in renewable energy technology. The new battery design could store more power with fewer materials. The research will be published in the journal Nature next month, pending peer review.",
        "url": "https://www.mit.edu/news",
        "expected": "REAL",
        "confidence": "90-95%"
    },
    {
        "category": "Community News",
        "text": "A family was rescued from a house fire this morning. Local firefighters worked for three hours to save all five family members. The community has started a fundraiser to help the family rebuild. The family expressed gratitude for the quick response from emergency services.",
        "url": "https://local-news.gov",
        "expected": "REAL",
        "confidence": "90-95%"
    },
    {
        "category": "Economics News",
        "text": "The central bank announced today that inflation rates have stabilized at 5.2% for the second consecutive quarter. Economists attribute this to improved supply chain management and controlled monetary policy. The stock market responded positively to the news.",
        "url": "https://www.reuters.com/business",
        "expected": "REAL",
        "confidence": "88-93%"
    },
    {
        "category": "Sports News",
        "text": "The national football team defeated their rivals 3-2 in yesterday's match. The winning goal was scored in the 89th minute by veteran player Ahmed Hassan. The team will advance to the championship finals next week.",
        "url": "https://sports-news.com",
        "expected": "REAL",
        "confidence": "85-90%"
    },
]

# ====================================================
# UNCERTAIN/DOUBTFUL EXAMPLES (Will show as DOUBTFUL)
# ====================================================

DOUBTFUL_NEWS_EXAMPLES = [
    {
        "category": "Opinion with Keywords",
        "text": "Some experts believe the new policy could have shocking consequences. The government is making incredible discoveries in technology. People are amazed by the stunning results. More research is needed to understand the full impact.",
        "url": "https://example.com",
        "expected": "DOUBTFUL",
        "confidence": "50-60%"
    },
    {
        "category": "Mixed Signals",
        "text": "BREAKING NEWS: Scientists discover amazing health benefits! However, more studies are needed before widespread recommendations. The initial research shows promise but requires additional verification.",
        "url": "https://uncertain.com",
        "expected": "DOUBTFUL",
        "confidence": "55-65%"
    },
    {
        "category": "Emotional News",
        "text": "The community was shocked and heartbroken by the terrible tragedy. Residents expressed their horror at the incident. Many people are devastated by this unbelievable disaster. Officials are investigating the situation.",
        "url": "https://news.com",
        "expected": "DOUBTFUL or REAL",
        "confidence": "50-70%"
    },
]

# ====================================================
# HOW TO TEST
# ====================================================

if __name__ == "__main__":
    print("="*70)
    print("FAKE NEWS DETECTION - TEST EXAMPLES")
    print("="*70)
    
    print("\n[FAKE NEWS EXAMPLES]")
    for i, example in enumerate(FAKE_NEWS_EXAMPLES, 1):
        print(f"\n{i}. {example['category']}")
        print(f"   Text: {example['text'][:60]}...")
        print(f"   URL: {example['url']}")
        print(f"   Expected: {example['expected']} ({example['confidence']})")
    
    print("\n" + "="*70)
    print("[REAL NEWS EXAMPLES]")
    for i, example in enumerate(REAL_NEWS_EXAMPLES, 1):
        print(f"\n{i}. {example['category']}")
        print(f"   Text: {example['text'][:60]}...")
        print(f"   URL: {example['url']}")
        print(f"   Expected: {example['expected']} ({example['confidence']})")
    
    print("\n" + "="*70)
    print("[DOUBTFUL EXAMPLES]")
    for i, example in enumerate(DOUBTFUL_NEWS_EXAMPLES, 1):
        print(f"\n{i}. {example['category']}")
        print(f"   Text: {example['text'][:60]}...")
        print(f"   URL: {example['url']}")
        print(f"   Expected: {example['expected']} ({example['confidence']})")
    
    print("\n" + "="*70)
    print("HOW TO TEST WITH THE API")
    print("="*70)
    print("""
1. Start the AI service:
   cd ai
   python app.py

2. In another terminal, test with curl:
   curl -X POST http://localhost:5000/predict \\
     -H "Content-Type: application/json" \\
     -d '{
       "text": "Your test text here",
       "url": "https://example.com"
     }'

3. Or use Python:
   import requests
   response = requests.post('http://localhost:5000/predict', json={
       "text": "Your test text",
       "url": "https://example.com"
   })
   print(response.json())
""")
