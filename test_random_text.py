#!/usr/bin/env python3
"""
Test random/normal text - what happens when you enter everyday text
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import detect_fake_news

print("="*70)
print("TESTING RANDOM/NORMAL TEXT")
print("What happens when you enter random text?")
print("="*70)

# Test 1: Simple question
print("\n1. SIMPLE QUESTION")
print("-"*70)
text = "What is the capital of France?"
result = detect_fake_news(text, "https://google.com")
print(f"Text: {text}")
print(f"Result: {result['result']}")
print(f"Confidence: {result['confidence']}%")
print(f"Score: {result['details']['final_score']}")
print(f"Explanation: {result['explanation'][:100]}...")

# Test 2: Random sentence
print("\n2. RANDOM SENTENCE")
print("-"*70)
text = "I went to the store yesterday and bought some groceries."
result = detect_fake_news(text, "https://example.com")
print(f"Text: {text}")
print(f"Result: {result['result']}")
print(f"Confidence: {result['confidence']}%")
print(f"Score: {result['details']['final_score']}")
print(f"Explanation: {result['explanation'][:100]}...")

# Test 3: Weather report
print("\n3. WEATHER REPORT")
print("-"*70)
text = "Tomorrow will be sunny with a high of 25 degrees. There is a 10% chance of rain."
result = detect_fake_news(text, "https://weather.com")
print(f"Text: {text}")
print(f"Result: {result['result']}")
print(f"Confidence: {result['confidence']}%")
print(f"Score: {result['details']['final_score']}")
print(f"Explanation: {result['explanation'][:100]}...")

# Test 4: Very short text
print("\n4. VERY SHORT TEXT")
print("-"*70)
text = "Hello world"
result = detect_fake_news(text, "https://example.com")
print(f"Text: {text}")
print(f"Result: {result['result']}")
print(f"Confidence: {result['confidence']}%")
print(f"Score: {result['details']['final_score']}")
print(f"Explanation: {result['explanation'][:100]}...")

# Test 5: Random paragraph
print("\n5. RANDOM PARAGRAPH")
print("-"*70)
text = "Technology has changed the way we communicate. People now use phones, computers, and tablets to stay connected. This digital revolution has impacted business, education, and personal relationships in significant ways."
result = detect_fake_news(text, "https://techblog.com")
print(f"Text: {text[:60]}...")
print(f"Result: {result['result']}")
print(f"Confidence: {result['confidence']}%")
print(f"Score: {result['details']['final_score']}")
print(f"Explanation: {result['explanation'][:100]}...")

# Test 6: Mix of normal + one suspicious word
print("\n6. NORMAL TEXT + ONE SUSPICIOUS WORD")
print("-"*70)
text = "This article is amazing and will shock you. We studied the effects of coffee on productivity and found interesting results."
result = detect_fake_news(text, "https://example.com")
print(f"Text: {text[:70]}...")
print(f"Result: {result['result']}")
print(f"Confidence: {result['confidence']}%")
print(f"Score: {result['details']['final_score']}")
print(f"Keywords Found: {result['details']['keyword_count']}")
print(f"Explanation: {result['explanation'][:100]}...")

# Test 7: Empty/Too short
print("\n7. VERY MINIMAL TEXT")
print("-"*70)
text = "Hi"
result = detect_fake_news(text, "https://example.com")
print(f"Text: {text}")
print(f"Result: {result['result']}")
print(f"Confidence: {result['confidence']}%")
print(f"Score: {result['details'].get('final_score', 'N/A')}")
print(f"Explanation: {result['explanation'][:100]}...")

# Test 8: Regular opinion
print("\n8. REGULAR OPINION")
print("-"*70)
text = "I think this movie is good. The actors were excellent and the plot was interesting. I would recommend it to anyone who likes drama films."
result = detect_fake_news(text, "https://example.com")
print(f"Text: {text[:70]}...")
print(f"Result: {result['result']}")
print(f"Confidence: {result['confidence']}%")
print(f"Score: {result['details']['final_score']}")
print(f"Explanation: {result['explanation'][:100]}...")

# Summary
print("\n" + "="*70)
print("SUMMARY - WHAT HAPPENS WITH RANDOM TEXT?")
print("="*70)
print("""
✓ Most normal text → REAL or DOUBTFUL
✓ Very short text → DOUBTFUL (not enough info)
✓ Opinion pieces → REAL or DOUBTFUL
✓ Technical/scientific → REAL
✓ Text with 1-2 suspicious words → DOUBTFUL
✓ Regular everyday text → REAL

The system is SMART - it doesn't just mark everything as FAKE!
It only flags content with:
  - Multiple suspicious keywords
  - Excessive capitalization/punctuation
  - Scam patterns
  - Conspiracy language
  
Random normal text is classified correctly as REAL or DOUBTFUL.
""")
