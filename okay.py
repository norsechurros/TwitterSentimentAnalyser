import tweepy
import pandas as pd
from textblob import TextBlob

# Authenticate with Twitter API v2
def authenticate_twitter(api_key, api_secret, access_token, access_token_secret, bearer_token):
    client = tweepy.Client(bearer_token=bearer_token)
    return client

# Fetch tweets using Twitter API v2
def fetch_tweets_v2(client, query, max_tweets=100):
    tweets_data = []
    # Using recent_search endpoint
    response = client.search_recent_tweets(query=query, max_results=min(max_tweets, 100), tweet_fields=["created_at", "text", "lang"])
    for tweet in response.data:
        if tweet.lang == "en":  # Filter English tweets
            tweets_data.append({'created_at': tweet.created_at, 'text': tweet.text})
    return tweets_data

# Perform Sentiment Analysis
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Main Function
def main():
    # Input from user
    query = input("Enter the word to search for in tweets: ")
    max_tweets = int(input("Enter the maximum number of tweets to fetch (max 100): "))

    # Twitter API credentials
    API_KEY = "0VtB7LinPraubsVFi9LiMHIhN"
    API_SECRET = "8l1Mrr3CSqHsNVhBxrz6aSdkv5gY44eNBajjsXFNrpBmz2brOW"
    ACCESS_TOKEN = "1865741526384402432-2vs1Ht30SgUr3dtIy9agoxxUfJovyD"
    ACCESS_TOKEN_SECRET = "nR2rQdnjJFXKowtm1gSg4oXJAFLq2UDzAndcVR5GZjCa2"
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMu3xQEAAAAAMldkLetGBF3cXRu1LKq9C4IMwGs%3DDkryY1QRNnvCuQyLxi5TtpuQq2ja3gGrbWI7MPyuCz2bXEVgEa"  # Required for v2

    # Authenticate
    client = authenticate_twitter(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN)

    # Fetch tweets
    print("Fetching tweets...")
    tweets = fetch_tweets_v2(client, query, max_tweets)

    # Analyze sentiment
    print("Analyzing sentiment...")
    for tweet in tweets:
        tweet['sentiment'] = analyze_sentiment(tweet['text'])

    # Create a DataFrame
    df = pd.DataFrame(tweets)
    print(df)

    # Save to CSV
    df.to_csv("tweets_sentiment.csv", index=False)
    print("Saved to tweets_sentiment.csv")

# Run the script
if __name__ == "__main__":
    main()
