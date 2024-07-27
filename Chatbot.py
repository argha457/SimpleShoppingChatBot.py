import matplotlib.pyplot as plt
from collections import defaultdict
import re

# Emotion lexicon
emotion_lexicon = {
    # Positive emotions
    "happy": "Positive",
    "joy": "Positive",
    "love": "Positive",
    "excellent": "Positive",
    "good": "Positive",
    "great": "Positive",
    "wonderful": "Positive",
    "fantastic": "Positive",
    "amazing": "Positive",
    "awesome": "Positive",
    "pleasant": "Positive",
    "delightful": "Positive",
    "cheerful": "Positive",
    "blessed": "Positive",
    "content": "Positive",
    "satisfied": "Positive",
    "nice": "Positive",
    "brilliant": "Positive",
    "enjoy": "Positive",
    "enthusiastic": "Positive",
    "grateful": "Positive",
    "loved": "Positive",
    "admire": "Positive",
    "celebrate": "Positive",
    "excited": "Positive",
    "glad": "Positive",
    "proud": "Positive",
    "relaxed": "Positive",
    "safe": "Positive",
    "successful": "Positive",
    "fortunate": "Positive",
    "thrilled": "Positive",
    "optimistic": "Positive",
    "elated": "Positive",
    "helpful": "Positive",
    "useful": "Positive",
    # Neutral emotions
    "okay": "Neutral",
    "fine": "Neutral",
    "average": "Neutral",
    "calm": "Neutral",
    "cool": "Neutral",
    "steady": "Neutral",
    "so-so": "Neutral",
    "unremarkable": "Neutral",
    "normal": "Neutral",
    "indifferent": "Neutral",
    "moderate": "Neutral",
    "unmoved": "Neutral",
    "composed": "Neutral",
    "collected": "Neutral",
    "mild": "Neutral",
    "medium": "Neutral",
    "balanced": "Neutral",
    "not sad": "Neutral",
    "not angry": "Neutral",
    "not hate": "Neutral",
    "not bad": "Neutral",
    "not terrible": "Neutral",
    "not awful": "Neutral",
    "not horrible": "Neutral",
    "not poor": "Neutral",
    "not unhappy": "Neutral",
    "not upset": "Neutral",
    "not depressed": "Neutral",
    "not miserable": "Neutral",
    "not disappointed": "Neutral",
    "not frustrated": "Neutral",
    "not annoyed": "Neutral",
    "not furious": "Neutral",
    "not resentful": "Neutral",
    "not irritated": "Neutral",
    "not displeased": "Neutral",
    "not hurt": "Neutral",
    "not bitter": "Neutral",
    "not lonely": "Neutral",
    "not melancholy": "Neutral",
    "not gloomy": "Neutral",
    "not distressed": "Neutral",
    "not worried": "Neutral",
    "not anxious": "Neutral",
    "not fearful": "Neutral",
    "not insecure": "Neutral",
    "not helpless": "Neutral",
    "not overwhelmed": "Neutral",
    "not devastated": "Neutral",
    "not regretful": "Neutral",
    "not ashamed": "Neutral",
    "not guilty": "Neutral",
    "not worthless": "Neutral",
    "not exhausted": "Neutral",
    "not tired": "Neutral",
    "not bored": "Neutral",
    "not skeptical": "Neutral",
    "not confused": "Neutral",
    # Negative emotions
    "sad": "Negative",
    "angry": "Negative",
    "hate": "Negative",
    "bad": "Negative",
    "terrible": "Negative",
    "awful": "Negative",
    "horrible": "Negative",
    "poor": "Negative",
    "unhappy": "Negative",
    "upset": "Negative",
    "depressed": "Negative",
    "miserable": "Negative",
    "disappointed": "Negative",
    "frustrated": "Negative",
    "annoyed": "Negative",
    "furious": "Negative",
    "resentful": "Negative",
    "irritated": "Negative",
    "displeased": "Negative",
    "hurt": "Negative",
    "bitter": "Negative",
    "lonely": "Negative",
    "melancholy": "Negative",
    "gloomy": "Negative",
    "distressed": "Negative",
    "worried": "Negative",
    "anxious": "Negative",
    "fearful": "Negative",
    "insecure": "Negative",
    "helpless": "Negative",
    "overwhelmed": "Negative",
    "devastated": "Negative",
    "regretful": "Negative",
    "ashamed": "Negative",
    "guilty": "Negative",
    "worthless": "Negative",
    "exhausted": "Negative",
    "tired": "Negative",
    "bored": "Negative",
    "skeptical": "Negative",
    "confused": "Negative",
    "not happy": "Negative",
    "not joy": "Negative",
    "not love": "Negative",
    "not excellent": "Negative",
    "not good": "Negative",
    "not great": "Negative",
    "not wonderful": "Negative",
    "not fantastic": "Negative",
    "not amazing": "Negative",
    "not awesome": "Negative",
    "not pleasant": "Negative",
    "not delightful": "Negative",
    "not cheerful": "Negative",
    "not blessed": "Negative",
    "not content": "Negative",
    "not satisfied": "Negative",
    "not nice": "Negative",
    "not brilliant": "Negative",
    "not enjoy": "Negative",
    "not enthusiastic": "Negative",
    "not grateful": "Negative",
    "not loved": "Negative",
    "not admire": "Negative",
    "not celebrate": "Negative",
    "not excited": "Negative",
    "not glad": "Negative",
    "not proud": "Negative",
    "not relaxed": "Negative",
    "not safe": "Negative",
    "not successful": "Negative",
    "not fortunate": "Negative",
    "not thrilled": "Negative",
    "not optimistic": "Negative",
    "not elated": "Negative",
    "not useful": "Negative",
    "not helpful": "Negative"
}

def analyze_sentiment(text):
    # Normalize the text
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    
    # Initialize sentiment scores
    sentiment_counts = defaultdict(int)
    
    # Count emotions in the text
    for word in words:
        if word in emotion_lexicon:
            sentiment_counts[emotion_lexicon[word]] += 1
    
    total_words = sum(sentiment_counts.values())
    sentiment_scores = {sentiment: count / total_words for sentiment, count in sentiment_counts.items()} if total_words > 0 else {}
    
    # Determine the type of sentiment based on the highest score
    if sentiment_scores:
        sentiment_type = max(sentiment_scores, key=sentiment_scores.get)
    else:
        sentiment_type = "Neutral"
    
    return sentiment_type, sentiment_scores

def plot_sentiment_scores(sentiment_scores):
    categories = ['Positive', 'Neutral', 'Negative']
    scores = [sentiment_scores.get(category, 0) for category in categories]
    
    plt.bar(categories, scores, color=['green', 'blue', 'red'])
    plt.xlabel('Sentiment')
    plt.ylabel('Score')
    plt.title('Sentiment Analysis Scores')
    plt.ylim(0, 1)
    plt.show()

def chatbot():
    print("Welcome to the Shopping App Chatbot!")
    print("How can I assist you today?")
    print("1. Check order status")
    print("2. Return an order")
    print("3. Customer support")
    print("4. Exit")
    
    while True:
        user_input = input("Please enter the number of your choice: ")
        
        if user_input == '1':
            order_id = input("Please enter your order ID: ")
            print(f"Checking status for order ID: {order_id}...")
            print("Your order is in transit and will be delivered in a few days.")
        elif user_input == '2':
            order_id = input("Please enter your order ID for the return: ")
            reason = input("Please provide the reason for the return: ")
            print(f"Processing return for order ID: {order_id} due to '{reason}'.")
            print("Your return request has been processed. You will receive further instructions via email.")
        elif user_input == '3':
            issue = input("Please describe your issue: ")
            print(f"Connecting you to customer support for the issue: '{issue}'.")
            print("A customer support representative will contact you shortly.")
        elif user_input == '4':
            print("Thank you for using the Shopping App Chatbot.")
            feedback = input("Before you go, please provide your feedback about this chatbot: ")
            sentiment_type, sentiment_scores = analyze_sentiment(feedback)
            print(f"Sentiment Type: {sentiment_type}")
            print(f"Sentiment Scores: {sentiment_scores}")
            plot_sentiment_scores(sentiment_scores)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    chatbot()


