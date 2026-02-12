#!/usr/bin/env python3
"""
Comprehensive Fake News Detection Test Suite
Tests all scenarios without ML dependencies
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import detect_fake_news

def print_result(test_num, name, text, url, expected, result):
    """Pretty print test result"""
    print(f"\n{test_num}. {name.upper()}")
    print("-" * 70)
    print(f"Text: {text[:70]}...")
    print(f"URL: {url}")
    print(f"\nRESULT:")
    print(f"  Classification: {result['result']}")
    print(f"  Confidence: {result['confidence']}%")
    print(f"  Final Score: {result['details']['final_score']}")
    print(f"  Keyword Count: {result['details']['keyword_count']}")
    print(f"  Pattern Score: {result['details']['pattern_score']}")
    print(f"  Source Reliability: {result['details']['source_reliability']}")
    
    print(f"\nEXPECTED: {expected}")
    passed = (expected in result['result']) or (result['result'] in expected)
    status = '[PASS]' if passed else '[FAIL]'
    print(f"Status: {status}")
    print(f"Explanation: {result['explanation'][:150]}...")
    
    return passed

def main():
    print("=" * 70)
    print("COMPREHENSIVE FAKE NEWS DETECTION TEST SUITE")
    print("=" * 70)
    
    results = []
    
    # TEST 1: Obvious Fake News - Health Scam
    text1 = ("BREAKING: ONE WEIRD TRICK doctors HATE! Click here for FREE money NOW! "
            "This will SHOCK you! Guaranteed $1000 daily! Limited time offer!")
    url1 = "https://suspicious-site.com"
    result1 = detect_fake_news(text1, url1)
    passed1 = print_result(1, "Obvious Fake News (Health Scam)", text1, url1, "Fake", result1)
    results.append(("Obvious Fake", passed1))
    
    # TEST 2: Legitimate News - Medical Research
    text2 = ("According to a study published in the Journal of Medical Research, "
            "researchers found that regular exercise can improve cardiovascular health. "
            "The study followed 10,000 participants over five years.")
    url2 = "https://www.bbc.com/health/article"
    result2 = detect_fake_news(text2, url2)
    passed2 = print_result(2, "Legitimate News (BBC Source)", text2, url2, "Real", result2)
    results.append(("Legitimate News", passed2))
    
    # TEST 3: Clickbait Conspiracy
    text3 = ("The mainstream media is LYING to you! The SECRET GOVERNMENT doesn't want you "
            "to know the truth! Wake up, sheeple! This viral story will blow your mind! "
            "Share before it gets deleted!")
    url3 = "https://truth-revealed.com"
    result3 = detect_fake_news(text3, url3)
    passed3 = print_result(3, "Clickbait Conspiracy", text3, url3, "Doubtful or Fake", result3)
    results.append(("Clickbait Conspiracy", passed3))
    
    # TEST 4: Financial Scam
    text4 = ("URGENT! WIN CASH NOW! Guaranteed $1000 daily income with ZERO investment! "
            "This exclusive offer is available for LIMITED TIME ONLY! Act now! "
            "Free money waiting for you!")
    url4 = "https://get-rich-quick.com"
    result4 = detect_fake_news(text4, url4)
    passed4 = print_result(4, "Financial Scam", text4, url4, "Fake", result4)
    results.append(("Financial Scam", passed4))
    
    # TEST 5: Well-written Legitimate Article
    text5 = ("The city council approved a new environmental protection law yesterday. "
            "The measure received support from 256 lawmakers while 89 voted against it. "
            "Environmental groups praised the decision as a significant step toward "
            "reducing carbon emissions in the region.")
    url5 = "https://www.bbc.com/news"
    result5 = detect_fake_news(text5, url5)
    passed5 = print_result(5, "Well-written Legitimate Article", text5, url5, "Real", result5)
    results.append(("Well-written Article", passed5))
    
    # TEST 6: Weight Loss Scam
    text6 = ("SHOCKING: Lose 50 pounds in 3 days! Doctors HATE this one weird trick! "
            "This MIRACLE CURE has been banned by doctors! Click here NOW for FREE access! "
            "Limited time offer! Share before it gets deleted! No investment required!")
    url6 = "https://instant-diet-secrets.com"
    result6 = detect_fake_news(text6, url6)
    passed6 = print_result(6, "Weight Loss Scam", text6, url6, "Fake", result6)
    results.append(("Weight Loss Scam", passed6))
    
    # TEST 7: Emotional but Legitimate News
    text7 = ("A family was rescued from a house fire this morning. Local firefighters "
            "worked heroically to save all five family members. The community has started "
            "a fundraiser to help rebuild. The family expressed gratitude for the "
            "quick response from emergency services.")
    url7 = "https://local-news.gov"
    result7 = detect_fake_news(text7, url7)
    passed7 = print_result(7, "Emotional Legitimate News", text7, url7, "Real", result7)
    results.append(("Emotional News", passed7))
    
    # TEST 8: Short Doubtful Content
    text8 = "Some people think the new policy might have consequences."
    url8 = "https://example.com"
    result8 = detect_fake_news(text8, url8)
    passed8 = print_result(8, "Short Content", text8, url8, "Real or Doubtful", result8)
    results.append(("Short Content", passed8))
    
    # TEST 9: High-frequency repetition
    text9 = ("Click click click now now now! Free free free! Buy buy buy! "
            "Act act act immediately immediately immediately! Limited limited limited!")
    url9 = "https://spam-site.com"
    result9 = detect_fake_news(text9, url9)
    passed9 = print_result(9, "High Repetition Spam", text9, url9, "Fake or Doubtful", result9)
    results.append(("Spam Content", passed9))
    
    # TEST 10: News from Trusted Source
    text10 = ("Scientists at MIT announced a breakthrough in renewable energy technology. "
             "The new battery design could store more power with fewer materials. "
             "The research will be published in the journal Nature next month.")
    url10 = "https://www.mit.edu/news"
    result10 = detect_fake_news(text10, url10)
    passed10 = print_result(10, "Trusted Source (MIT)", text10, url10, "Real", result10)
    results.append(("MIT News", passed10))
    
    # SUMMARY
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    
    passed_count = sum(1 for _, p in results if p)
    total_count = len(results)
    
    for name, passed in results:
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status}: {name}")
    
    print("\n" + "=" * 70)
    print(f"TOTAL: {passed_count}/{total_count} tests passed ({passed_count*100//total_count}%)")
    print("=" * 70)
    
    if passed_count >= 8:
        print("\n[OK] System is working well! Most tests passing.")
    elif passed_count >= 6:
        print("\n[WARNING] System needs tuning. Some detection thresholds may need adjustment.")
    else:
        print("\n[ERROR] System needs review. Many tests failing.")

if __name__ == '__main__':
    main()
