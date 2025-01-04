import tweepy
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# 1. Get credentials from environment variables
bearer_token = os.getenv("BEARER_TOKEN")
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# 2. Authenticate to the Twitter API
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
    )

# 3.Test authentication
try:
    user = client.get_me()
    print(f"Authenticated as @{user.data.username}")
except Exception as e:
    print(f"Authentication error: {e}")

# 4.Define a query
# Set up hasthtags/ keywords to search for tweets about the movie Wicked (Example: #Wicked, #WickedMovie, #WickedMusical, #Elphaba, #Glinda)
query = "#Wicked -is:retweet lang:en"

# 5.Collect tweets and save them to a CSV file for analysis
# Specify parameters such as lnaguage (lang="en") amd exclude retweets (is:retweet) to avoid duplicates/
# Collect a sample of 100 tweets
tweets = client.search_recent_tweets(
    query=query,
    tweet_fields=["created_at", "author_id", "public_metrics", "text"],
    max_results=10
)

# Process tweets into a DataFrame
tweet_data =[]
for tweet in tweets.data:
    tweet_data.append({
        "id": tweet.id,
        "created_at": tweet.created_at,
        "author_id": tweet.author_id,
        "retweet_count": tweet.public_metrics["retweet_count"],
        "reply_count": tweet.public_metrics["reply_count"],
        "like_count": tweet.public_metrics["like_count"],
        "quote_count": tweet.public_metrics["quote_count"],
        "text": tweet.text
    })

# Save the tweet data to a CSV file
df = pd.DataFrame(tweet_data)
df.to_csv("wicked_tweets.csv", index=False)
print("Tweets saved to wicked_tweets.csv")

# 6.Clean and process tweets
# Remove URLs, hashtags, mentions, and emojis


# Perform sentiment analysis

# Visualize and analyze