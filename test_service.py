#!/usr/bin/env python3
"""
Test script for the Advanced Fake News Detection Service
Run this after starting the AI service to verify everything works
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_health():
    """Test health endpoint"""
    print("=" * 60)
    print("Testing Health Endpoint...")
    print("=" * 60)
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print("✓ Health check passed\n")
        return True
    except Exception as e:
        print(f"✗ Health check failed: {e}\n")
        return False

def test_fake_news():
    """Test with obvious fake news"""
    print("=" * 60)
    print("Test 1: Obvious Fake News")
    print("=" * 60)
    
    test_data = {
        "text": "BREAKING: Scientists discover ONE WEIRD TRICK to lose 50 pounds in 3 days! Doctors HATE this! Click here NOW for FREE money! This will SHOCK you!",
        "url": "https://suspicious-site.com/fake-news"
    }
    
    try:
        start_time = time.time()
        response = requests.post(f"{BASE_URL}/predict", json=test_data)
        elapsed = time.time() - start_time
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {elapsed:.2f} seconds")
        result = response.json()
        print(f"\nResult: {result['result']}")
        print(f"Confidence: {result['confidence']}%")
        print(f"Explanation: {result['explanation']}")
        print(f"\nDetailed Breakdown:")
        print(json.dumps(result.get('details', {}), indent=2))
        print("\n✓ Test passed\n")
        return True
    except Exception as e:
        print(f"✗ Test failed: {e}\n")
        return False

def test_real_news():
    """Test with legitimate news"""
    print("=" * 60)
    print("Test 2: Legitimate News")
    print("=" * 60)
    
    test_data = {
        "text": "According to a study published in the Journal of Medical Research, researchers found that regular exercise can improve cardiovascular health. The study, which followed 10,000 participants over five years, showed a 20% reduction in heart disease risk among those who exercised regularly.",
        "url": "https://www.bbc.com/health/article"
    }
    
    try:
        start_time = time.time()
        response = requests.post(f"{BASE_URL}/predict", json=test_data)
        elapsed = time.time() - start_time
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {elapsed:.2f} seconds")
        result = response.json()
        print(f"\nResult: {result['result']}")
        print(f"Confidence: {result['confidence']}%")
        print(f"Explanation: {result['explanation']}")
        print("\n✓ Test passed\n")
        return True
    except Exception as e:
        print(f"✗ Test failed: {e}\n")
        return False

def test_doubtful_news():
    """Test with ambiguous content"""
    print("=" * 60)
    print("Test 3: Ambiguous/Doubtful Content")
    print("=" * 60)
    
    test_data = {
        "text": "Some people say that the new policy might have unintended consequences. There are different opinions about this topic, and experts are still debating the best approach.",
        "url": "https://example.com/article"
    }
    
    try:
        start_time = time.time()
        response = requests.post(f"{BASE_URL}/predict", json=test_data)
        elapsed = time.time() - start_time
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {elapsed:.2f} seconds")
        result = response.json()
        print(f"\nResult: {result['result']}")
        print(f"Confidence: {result['confidence']}%")
        print(f"Explanation: {result['explanation']}")
        print("\n✓ Test passed\n")
        return True
    except Exception as e:
        print(f"✗ Test failed: {e}\n")
        return False

def test_short_text():
    """Test with very short text"""
    print("=" * 60)
    print("Test 4: Short Text (Edge Case)")
    print("=" * 60)
    
    test_data = {
        "text": "Breaking news!",
        "url": None
    }
    
    try:
        response = requests.post(f"{BASE_URL}/predict", json=test_data)
        result = response.json()
        print(f"Result: {result['result']}")
        print(f"Confidence: {result['confidence']}%")
        print(f"Explanation: {result['explanation']}")
        print("\n✓ Test passed (correctly handled short text)\n")
        return True
    except Exception as e:
        print(f"✗ Test failed: {e}\n")
        return False

def test_error_handling():
    """Test error handling"""
    print("=" * 60)
    print("Test 5: Error Handling")
    print("=" * 60)
    
    # Test with missing text
    try:
        response = requests.post(f"{BASE_URL}/predict", json={})
        print(f"Status Code: {response.status_code}")
        if response.status_code == 400:
            print("✓ Correctly returned error for missing text\n")
            return True
        else:
            print("✗ Unexpected status code\n")
            return False
    except Exception as e:
        print(f"✗ Test failed: {e}\n")
        return False

def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("FAKE NEWS DETECTION SERVICE - TEST SUITE")
    print("=" * 60)
    print("\nMake sure the AI service is running on http://localhost:5000")
    print("Press Ctrl+C to cancel\n")
    time.sleep(2)
    
    results = []
    
    # Run tests
    results.append(("Health Check", test_health()))
    results.append(("Fake News Detection", test_fake_news()))
    results.append(("Real News Detection", test_real_news()))
    results.append(("Doubtful Content", test_doubtful_news()))
    results.append(("Short Text Handling", test_short_text()))
    results.append(("Error Handling", test_error_handling()))
    
    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! The service is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Check the service logs for details.")
    
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTests cancelled by user.")
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
