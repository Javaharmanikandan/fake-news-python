#!/usr/bin/env python3
"""
Quick test script to verify detection is working correctly
Run this to test if the detection logic is properly classifying content
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from app import detect_fake_news

def test_detection():
    """Test various news samples"""
    
    print("=" * 70)
    print("FAKE NEWS DETECTION TEST")
    print("=" * 70)
    
    test_cases = [
        {
            "name": "Obvious Fake News",
            "text": "BREAKING: Scientists discover ONE WEIRD TRICK to lose 50 pounds in 3 days! Doctors HATE this! Click here NOW for FREE money! This will SHOCK you!",
            "url": "https://suspicious-site.com/fake-news",
            "expected": "Fake"
        },
        {
            "name": "Legitimate News",
            "text": "According to a study published in the Journal of Medical Research, researchers found that regular exercise can improve cardiovascular health. The study, which followed 10,000 participants over five years, showed a 20% reduction in heart disease risk among those who exercised regularly.",
            "url": "https://www.bbc.com/health/article",
            "expected": "Real or Doubtful"
        },
        {
            "name": "Normal News Article",
            "text": "The city council met yesterday to discuss the new budget proposal. Mayor Johnson presented a plan that would increase funding for public schools while maintaining current tax rates. The proposal will be voted on next month.",
            "url": "https://example.com/news",
            "expected": "Doubtful or Real"
        },
        {
            "name": "Suspicious Content",
            "text": "URGENT! They don't want you to know this secret! Click here to discover the shocking truth about what's really happening. Share before it gets deleted!",
            "url": "https://conspiracy-site.com",
            "expected": "Fake"
        },
        {
            "name": "Neutral Content",
            "text": "The weather forecast for tomorrow shows partly cloudy skies with a high of 72 degrees. There is a 30% chance of rain in the afternoon.",
            "url": None,
            "expected": "Doubtful or Real"
        }
    ]
    
    results = []
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{'='*70}")
        print(f"Test {i}: {test['name']}")
        print(f"{'='*70}")
        print(f"Text: {test['text'][:100]}...")
        print(f"URL: {test['url']}")
        print(f"Expected: {test['expected']}")
        print("-" * 70)
        
        try:
            result = detect_fake_news(test['text'], test['url'])
            
            print(f"Result: {result['result']}")
            print(f"Confidence: {result['confidence']}%")
            print(f"Source Credibility: {result['source_credibility']}")
            print(f"Explanation: {result['explanation'][:200]}...")
            
            if result.get('details'):
                details = result['details']
                print(f"\nDetails:")
                print(f"  - Keyword Count: {details.get('keyword_count', 0)}")
                print(f"  - Pattern Score: {details.get('pattern_score', 0)}")
                print(f"  - Final Score: {details.get('final_score', 0)}")
                if details.get('ml_classification'):
                    ml = details['ml_classification']
                    print(f"  - ML Classification: {ml.get('label', 'N/A')} ({ml.get('score', 0):.2f})")
            
            # Check if result matches expectation
            expected_results = test['expected'].split(' or ')
            match = result['result'] in expected_results
            status = "✓ PASS" if match else "✗ FAIL"
            print(f"\n{status} - Expected one of: {expected_results}, Got: {result['result']}")
            
            results.append({
                'test': test['name'],
                'expected': test['expected'],
                'got': result['result'],
                'confidence': result['confidence'],
                'passed': match
            })
            
        except Exception as e:
            print(f"✗ ERROR: {e}")
            import traceback
            traceback.print_exc()
            results.append({
                'test': test['name'],
                'expected': test['expected'],
                'got': 'ERROR',
                'confidence': 0,
                'passed': False
            })
    
    # Summary
    print(f"\n{'='*70}")
    print("TEST SUMMARY")
    print(f"{'='*70}")
    
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    
    for r in results:
        status = "✓" if r['passed'] else "✗"
        print(f"{status} {r['test']}: Expected {r['expected']}, Got {r['got']} ({r['confidence']}%)")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Detection is working correctly.")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Review the detection logic.")
    
    print("=" * 70)

if __name__ == "__main__":
    try:
        test_detection()
    except KeyboardInterrupt:
        print("\n\nTest cancelled by user.")
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
