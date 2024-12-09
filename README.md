# Twitter Sentiment Analysis Script

This Python script allows you to search for tweets containing a specific keyword from the past 7 days and perform sentiment analysis on them. The tool uses the Twitter API v2 to fetch tweets and TextBlob for analyzing sentiment polarity (Positive, Negative, Neutral). Results are saved to a CSV file for easy analysis.
Features

    Fetch tweets containing a specific keyword from the past 7 days using the Twitter API v2.
    Perform sentiment analysis on the tweets using TextBlob.
    Supports user inputs for:
        Keyword to search for.
        Maximum number of tweets to fetch (up to 100 per request).
    Outputs the results to a CSV file (tweets_sentiment.csv) with the following columns:
        Created At: Timestamp of the tweet.
        Text: The content of the tweet.
        Sentiment: Sentiment label (Positive, Negative, Neutral).
    Simple and lightweight, with minimal dependencies.

# Requirements

    Python 3.7 or above.
    Twitter Developer account with Elevated Access to API v2.
    Required Python libraries:
        tweepy: For interacting with the Twitter API.
        textblob: For sentiment analysis.
        pandas: For organizing tweet data.

# Installation

    Clone the repository:

git clone https://github.com/norsechurros/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis

Install the required Python packages:

    pip install tweepy textblob pandas

    Set up your Twitter API credentials:
        Obtain your API Key, API Secret, Access Token, Access Token Secret, and Bearer Token from the Twitter Developer Portal.
        Replace the placeholder values in the script with your credentials.

# Usage

    Run the script:

    python sentiment_analysis.py

    Enter the required inputs when prompted:
        Keyword to search for (e.g., "climate change").
        Maximum number of tweets to fetch (e.g., 50).

    View the results in the terminal or check the tweets_sentiment.csv file for saved output.

Output Example
Created At	Text	Sentiment
2024-12-08 15:23:11	"The world is changing rapidly due to climate..."	Positive
2024-12-08 14:10:32	"I'm worried about the impact of climate change."	Negative
Notes

    The script uses Twitter API v2's recent_search endpoint, which has a limit of 100 tweets per request.
    Ensure compliance with Twitter's API usage guidelines when running the script.
    Modify the script to implement pagination if you need to fetch more than 100 tweets.

# Future Improvements

    Add real-time streaming for live tweet analysis.
    Support for additional languages.
    Advanced sentiment analysis with libraries like VADER or transformers.

#License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this script.
