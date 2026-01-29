# Fake News Detection - Test Examples Guide

This guide shows you exactly what type of news to submit to get different classification results.

## 🚨 FAKE NEWS Examples (Will be classified as "Fake")

### Example 1: Clickbait with Suspicious Keywords
```
BREAKING: Scientists discover ONE WEIRD TRICK to lose 50 pounds in 3 days! Doctors HATE this secret! Click here NOW for FREE money! This will SHOCK you! Share before it gets deleted!
```
**Why it's fake:**
- Contains keywords: "one weird trick", "doctors hate", "click here", "free money", "shocking"
- Excessive capitalization
- Urgency manipulation ("NOW", "BREAKING")
- URL: `https://suspicious-site.com`

### Example 2: Health Scam
```
URGENT! They don't want you to know about this MIRACLE CURE! One secret remedy that cures ALL diseases! Pharmaceutical companies are hiding this from you! Click here to learn the shocking truth!
```
**Why it's fake:**
- Keywords: "miracle cure", "they don't want you to know", "secret", "shocking truth"
- Conspiracy language
- Excessive exclamation marks
- URL: `https://fake-health-news.com`

### Example 3: Financial Scam
```
WIN CASH NOW! Guaranteed $1000 daily income! No investment required! Act now - limited time offer! Click here for instant results! Free money waiting for you!
```
**Why it's fake:**
- Keywords: "win cash", "guaranteed", "free money", "click here", "instant", "act now"
- Financial scam patterns
- Urgency manipulation
- URL: `https://get-rich-quick.com`

### Example 4: Conspiracy Theory
```
The mainstream media is LYING to you! The secret government doesn't want you to know the truth about what's really happening. Wake up, sheeple! The deep state is controlling everything!
```
**Why it's fake:**
- Keywords: "secret government", "they don't want you to know", "wake up"
- Conspiracy language
- Negative sentiment
- URL: `https://conspiracy-theory-site.com`

### Example 5: Viral Hoax
```
SHOCKING! You won't believe what happened! This viral story will blow your mind! Share before it gets deleted! Breaking: You won't believe this!
```
**Why it's fake:**
- Keywords: "shocking", "you won't believe", "viral", "share before deleted", "breaking"
- Clickbait patterns
- Excessive capitalization
- Emotional manipulation

---

## ✅ REAL NEWS Examples (Will be classified as "Real")

### Example 1: Legitimate Health Study
```
According to a study published in the Journal of Medical Research, researchers found that regular exercise can improve cardiovascular health. The study, which followed 10,000 participants over five years, showed a 20% reduction in heart disease risk among those who exercised regularly. The findings were published in the peer-reviewed journal last month.
```
**Why it's real:**
- Professional language
- Cites specific study and journal
- No suspicious keywords
- URL: `https://www.bbc.com/health/article` (trusted source)
- Neutral, factual tone

### Example 2: Standard News Report
```
The city council met yesterday to discuss the new budget proposal. Mayor Johnson presented a plan that would increase funding for public schools while maintaining current tax rates. The proposal will be voted on next month during the regular council meeting.
```
**Why it's real:**
- Factual reporting
- No emotional manipulation
- Professional writing
- URL: `https://www.reuters.com/local-news` (trusted source)
- Clear, neutral language

### Example 3: Weather Report
```
The National Weather Service issued a forecast for tomorrow showing partly cloudy skies with a high of 72 degrees Fahrenheit. There is a 30% chance of rain in the afternoon, with winds expected to be light at 5-10 miles per hour.
```
**Why it's real:**
- Factual information
- No suspicious patterns
- Professional tone
- URL: `https://www.weather.gov/forecast` (trusted source)

### Example 4: Business News
```
TechCorp announced today that its quarterly earnings exceeded expectations, with revenue increasing by 15% compared to the same period last year. The company's stock price rose 3% in after-hours trading following the announcement.
```
**Why it's real:**
- Professional business reporting
- Specific data and facts
- No emotional language
- URL: `https://www.wsj.com/business` (trusted source)

### Example 5: Science News
```
A team of researchers from Harvard University published findings in Nature journal showing that a new drug compound shows promise in treating Alzheimer's disease. The study involved 500 patients over two years and showed a 25% improvement in cognitive function.
```
**Why it's real:**
- Cites reputable institution (Harvard)
- Mentions peer-reviewed journal (Nature)
- Specific research details
- Professional scientific language
- URL: `https://www.nature.com/articles` (trusted source)

---

## ⚠️ DOUBTFUL Examples (Will be classified as "Doubtful")

### Example 1: Ambiguous Content
```
Some people say that the new policy might have unintended consequences. There are different opinions about this topic, and experts are still debating the best approach. More research is needed to determine the full impact.
```
**Why it's doubtful:**
- Vague language
- No specific sources
- Neutral tone
- No clear indicators either way

### Example 2: Opinion Piece
```
In my opinion, the current economic situation requires careful consideration. While some experts suggest one approach, others recommend a different strategy. The debate continues among policymakers.
```
**Why it's doubtful:**
- Opinion-based
- No clear facts or sources
- Neutral language
- Not clearly fake or real

### Example 3: Short Content
```
Breaking news about the event. More details to follow.
```
**Why it's doubtful:**
- Too short to analyze properly
- No specific information
- Cannot determine authenticity

---

## 📊 Quick Reference: What Triggers Each Classification

### To Get "FAKE" Classification:
✅ Use suspicious keywords (see list below)
✅ Add excessive capitalization (ALL CAPS)
✅ Include urgency words (URGENT, NOW, ACT NOW)
✅ Use emotional manipulation (SHOCKING, YOU WON'T BELIEVE)
✅ Add clickbait phrases (CLICK HERE, FREE MONEY)
✅ Use conspiracy language (THEY DON'T WANT YOU TO KNOW)
✅ Include multiple exclamation marks (!!!)
✅ Use untrusted or suspicious URLs

### To Get "REAL" Classification:
✅ Use professional, factual language
✅ Cite specific sources (studies, institutions, journals)
✅ Write in neutral, objective tone
✅ Use proper grammar and punctuation
✅ Include specific data and facts
✅ Use trusted news source URLs (BBC, Reuters, AP, etc.)
✅ Avoid emotional language
✅ Use complete sentences

### To Get "DOUBTFUL" Classification:
✅ Use vague or ambiguous language
✅ No specific sources cited
✅ Short or incomplete content
✅ Neutral tone with no clear indicators
✅ Opinion-based content
✅ Unknown or medium-credibility sources

---

## 🔑 Key Suspicious Keywords That Trigger "Fake"

**Financial Scams:**
- free money
- win cash
- guaranteed income
- no investment required
- get rich quick
- earn $1000 daily
- work from home scam

**Health Scams:**
- miracle cure
- doctors hate
- one weird trick
- lose weight fast
- cure all diseases
- secret remedy
- pharmaceutical companies hide

**Clickbait:**
- click here
- you won't believe
- shocking truth
- they don't want you to know
- secret government
- breaking: you won't believe
- viral
- share before deleted
- this will shock you

**Urgency/Manipulation:**
- urgent
- act now
- limited time
- exclusive offer
- no questions asked
- guaranteed
- 100% proven
- instant results

**Conspiracy:**
- mainstream media lies
- cover-up
- hidden truth
- they're hiding
- wake up
- sheeple
- deep state
- illuminati

---

## 🧪 How to Test

1. **Copy one of the examples above**
2. **Submit it through your frontend**
3. **Check the result:**
   - Fake examples → Should show "Fake" with confidence 60-95%
   - Real examples → Should show "Real" with confidence 80-95%
   - Doubtful examples → Should show "Doubtful" with confidence 40-60%

4. **Check the explanation** to see which factors triggered the classification

---

## 💡 Tips for Testing

1. **Mix and match**: Combine elements from fake news examples to create your own
2. **Check the details**: Look at the "details" field in the response to see the breakdown
3. **Try variations**: Modify examples slightly to see how it affects the score
4. **Use real URLs**: For "Real" examples, use actual trusted news source URLs
5. **Use suspicious URLs**: For "Fake" examples, use made-up or suspicious domain names

---

## 📝 Example Test Cases

### Test Case 1: Obvious Fake
```
Text: "BREAKING: ONE WEIRD TRICK doctors HATE! Click here for FREE money NOW! This will SHOCK you!"
URL: "https://suspicious-site.com"
Expected: FAKE (confidence: 75-90%)
```

### Test Case 2: Legitimate News
```
Text: "According to a study published in the Journal of Medical Research, regular exercise improves cardiovascular health. The study followed 10,000 participants over five years."
URL: "https://www.bbc.com/health"
Expected: REAL (confidence: 80-95%)
```

### Test Case 3: Ambiguous
```
Text: "Some people think the new policy might have consequences. Experts are still debating."
URL: "https://example.com"
Expected: DOUBTFUL (confidence: 45-55%)
```

---

Use these examples to test your system and understand how different content types are classified!
