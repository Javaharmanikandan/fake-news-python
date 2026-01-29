#!/usr/bin/env python3
"""
Quick test to verify detection thresholds are working
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import detect_fake_news

print("=" * 70)
print("QUICK DETECTION TEST")
print("=" * 70)

# Test 1: Obvious Fake
print("\n1. TESTING OBVIOUS FAKE NEWS:")
print("-" * 70)
fake_text = "BREAKING: ONE WEIRD TRICK doctors HATE! Click here for FREE money NOW! This will SHOCK you!"
fake_url = "https://suspicious-site.com"
result = detect_fake_news(fake_text, fake_url)
print(f"Text: {fake_text[:60]}...")
print(f"Result: {result['result']}")
print(f"Confidence: {result['confidence']}%")
print(f"Final Score: {result['details']['final_score']}")
print(f"Keyword Count: {result['details']['keyword_count']}")
print(f"Pattern Score: {result['details']['pattern_score']}")
print(f"Expected: FAKE")
print(f"Status: {'✓ PASS' if result['result'] == 'Fake' else '✗ FAIL'}")

# Test 2: Legitimate News
print("\n2. TESTING LEGITIMATE NEWS:")
print("-" * 70)
real_text = "According to a study published in the Journal of Medical Research, researchers found that regular exercise can improve cardiovascular health. The study followed 10,000 participants over five years."
real_url = "https://www.bbc.com/health/article"
result2 = detect_fake_news(real_text, real_url)
print(f"Text: {real_text[:60]}...")
print(f"Result: {result2['result']}")
print(f"Confidence: {result2['confidence']}%")
print(f"Final Score: {result2['details']['final_score']}")
print(f"Keyword Count: {result2['details']['keyword_count']}")
print(f"Pattern Score: {result2['details']['pattern_score']}")
print(f"Expected: REAL")
print(f"Status: {'✓ PASS' if result2['result'] == 'Real' else '✗ FAIL'}")

# Test 3: Normal Content
print("\n3. TESTING NORMAL CONTENT:")
print("-" * 70)
normal_text = "Some people think the new policy might have consequences. Experts are still debating."
normal_url = "https://example.com"
result3 = detect_fake_news(normal_text, normal_url)
print(f"Text: {normal_text[:60]}...")
print(f"Result: {result3['result']}")
print(f"Confidence: {result3['confidence']}%")
print(f"Final Score: {result3['details']['final_score']}")
print(f"Keyword Count: {result3['details']['keyword_count']}")
print(f"Pattern Score: {result3['details']['pattern_score']}")
print(f"Expected: REAL or DOUBTFUL")
print(f"Status: {'✓ PASS' if result3['result'] in ['Real', 'Doubtful'] else '✗ FAIL'}")

print("\n" + "=" * 70)
print("SUMMARY:")
print("=" * 70)
print(f"Fake News Test: {'✓ PASS' if result['result'] == 'Fake' else '✗ FAIL'}")
print(f"Real News Test: {'✓ PASS' if result2['result'] == 'Real' else '✗ FAIL'}")
print(f"Normal Content Test: {'✓ PASS' if result3['result'] in ['Real', 'Doubtful'] else '✗ FAIL'}")
