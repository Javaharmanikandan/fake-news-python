# Detection Debugging Guide

## Current Thresholds

- **FAKE**: Score >= 35
- **REAL**: Score <= 20 (or <= 15 from trusted source)
- **DOUBTFUL**: 20 < Score < 35

## Scoring Breakdown

### How Points Are Awarded:

1. **Keywords** (up to 40 points):
   - First 3 keywords: 8 points each = 24 points
   - Additional keywords: 6 points each
   - Example: 4 keywords = 24 + 6 = 30 points

2. **Linguistic Patterns** (up to 35 points):
   - Pattern score × 0.35
   - Example: Pattern score 50 = 17.5 points

3. **Source Reliability** (up to 25 points):
   - Low source: +25 points
   - High source: -20 points

4. **Sentiment** (up to 15 points):
   - Extreme sentiment: +15 points
   - Neutral sentiment: -5 points

5. **Readability** (up to 15 points):
   - Suspicion score × 0.15

6. **ML Model** (up to 20 points):
   - Strong negative: +20 points
   - Strong positive (clickbait): +10 points
   - Moderate positive: -5 points

7. **Fact-checking** (up to 15 points):
   - Needs verification: +15 points

8. **Similarity** (up to 20 points):
   - Known fake patterns: up to 20 points

9. **Bonuses**:
   - Multiple indicators (2+ keywords + patterns): +10 points
   - Many keywords (3+): +5 points

## Example Calculations

### Example 1: Obvious Fake News
```
Text: "BREAKING: ONE WEIRD TRICK doctors HATE! Click here for FREE money NOW!"
Keywords: 4 matches ("one weird trick", "doctors hate", "click here", "free money")
Patterns: Excessive caps, exclamation marks = 35 points
Source: suspicious-site.com = low = +25 points

Calculation:
- Keywords: 24 + 6 = 30 points
- Patterns: 35 × 0.35 = 12.25 points
- Source: +25 points
- Bonus (4 keywords): +5 points
- Bonus (multiple indicators): +10 points
Total: ~82 points → FAKE (confidence: ~90%)
```

### Example 2: Legitimate News
```
Text: "According to a study published in the Journal of Medical Research..."
Keywords: 0 matches
Patterns: Normal writing = 5 points
Source: bbc.com = high = -20 points

Calculation:
- Keywords: 0 points
- Patterns: 5 × 0.35 = 1.75 points
- Source: -20 points
- Clean content bonus: -8 points
Total: ~-26 points → Clamped to 0 → REAL (confidence: ~90%)
```

### Example 3: Normal Content
```
Text: "Some people think the new policy might have consequences."
Keywords: 0 matches
Patterns: Normal writing = 10 points
Source: example.com = medium = 0 points

Calculation:
- Keywords: 0 points
- Patterns: 10 × 0.35 = 3.5 points
- Source: 0 points
- Clean content bonus: -8 points
Total: ~-4 points → Clamped to 0 → REAL (confidence: ~85%)
```

Wait, that's wrong. Let me recalculate...

Actually, if score is 0-20, it should be REAL. But we're subtracting too much. Let me check the logic again.

## Testing Your Detection

1. **Test with obvious fake:**
   - Use 3+ suspicious keywords
   - Add ALL CAPS
   - Use suspicious URL
   - Should get score >= 35 → FAKE

2. **Test with legitimate news:**
   - Professional language
   - No keywords
   - Trusted source URL
   - Should get score <= 20 → REAL

3. **Test with ambiguous:**
   - Vague language
   - No keywords
   - Unknown source
   - Should get score 20-35 → DOUBTFUL

## If Everything Shows "Doubtful"

Check:
1. Are keywords being detected? (Check `details.keyword_count`)
2. Are patterns being detected? (Check `details.pattern_score`)
3. What's the final score? (Check `details.final_score`)
4. Is the source being recognized? (Check `source_credibility`)

## Quick Fix Test

Try this obvious fake news:
```
BREAKING: ONE WEIRD TRICK doctors HATE! Click here for FREE money NOW! This will SHOCK you!
URL: https://suspicious-site.com
```

This should definitely be FAKE with high confidence.
