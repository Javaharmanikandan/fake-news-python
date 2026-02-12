#!/usr/bin/env python3
"""
Quick Test Script - Test examples against the detection system
Run: python test_with_examples.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import detect_fake_news
from test_examples import FAKE_NEWS_EXAMPLES, REAL_NEWS_EXAMPLES, DOUBTFUL_NEWS_EXAMPLES

def test_category(category_name, examples):
    """Test a category of examples"""
    print(f"\n{'='*70}")
    print(f"{category_name}")
    print('='*70)
    
    passed = 0
    total = len(examples)
    
    for i, example in enumerate(examples, 1):
        print(f"\n{i}. {example['category']}")
        print(f"   Text: {example['text'][:80]}...")
        
        # Run detection
        result = detect_fake_news(example['text'], example['url'])
        
        # Check if result matches expected
        expected = example['expected'].split(' or ')[0]  # Get first option
        actual = result['result']
        
        match = expected in actual or actual in expected
        status = "[PASS]" if match else "[FAIL]"
        
        print(f"   Expected: {example['expected']} ({example['confidence']})")
        print(f"   Got: {actual} ({result['confidence']}%)")
        print(f"   Score: {result['details']['final_score']}")
        print(f"   Status: {status}")
        
        if match:
            passed += 1
    
    print(f"\n{category_name} Results: {passed}/{total} passed")
    return passed, total

def main():
    print("="*70)
    print("FAKE NEWS DETECTION - TESTING WITH EXAMPLES")
    print("="*70)
    
    # Test fake news
    fake_passed, fake_total = test_category("[FAKE NEWS EXAMPLES]", FAKE_NEWS_EXAMPLES)
    
    # Test real news
    real_passed, real_total = test_category("[REAL NEWS EXAMPLES]", REAL_NEWS_EXAMPLES)
    
    # Test doubtful
    doubtful_passed, doubtful_total = test_category("[DOUBTFUL EXAMPLES]", DOUBTFUL_NEWS_EXAMPLES)
    
    # Summary
    total_passed = fake_passed + real_passed + doubtful_passed
    total_tests = fake_total + real_total + doubtful_total
    
    print(f"\n{'='*70}")
    print("SUMMARY")
    print('='*70)
    print(f"Fake News:   {fake_passed}/{fake_total} passed")
    print(f"Real News:   {real_passed}/{real_total} passed")
    print(f"Doubtful:    {doubtful_passed}/{doubtful_total} passed")
    print(f"\nTotal: {total_passed}/{total_tests} passed ({total_passed*100//total_tests}%)")
    print('='*70)
    
    if total_passed >= total_tests - 2:
        print("\n[OK] System is working well!")
    else:
        print("\n[WARNING] Some tests failed. Check detection thresholds.")

if __name__ == '__main__':
    main()
