
from textblob import TextBlob
import nltk
import string

nltk.download('punkt')  

def clean_text(text):
    """
    Lowercases text and removes punctuation.
    """
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

def get_sentiment(text):
    """
    Returns sentiment label and polarity score.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return 'Positive', polarity
    elif polarity < 0:
        return 'Negative', polarity
    else:
        return 'Neutral', polarity

print("🔍 Live Sentiment Analysis is ready.")
print("Type your sentence and press Enter.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("🗣️ Enter comment: ")
    if user_input.lower() == 'exit':
        print("\n✅ Session ended. Goodbye!")
        break

    cleaned = clean_text(user_input)
    sentiment, score = get_sentiment(cleaned)

    print(f"🧹 Cleaned Comment: {cleaned}")
    print(f"📊 Sentiment: {sentiment}")
    print(f"📈 Polarity Score: {score:.2f}\n")