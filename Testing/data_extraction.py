import tweepy
import os
from dotenv import load_dotenv
import pandas as pd
import time
from tweepy.errors import TooManyRequests

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

# 3. Test authentication
try:
    user = client.get_me()
    print(f"Authenticated as @{user.data.username}")
except Exception as e:
    print(f"Authentication error: {e}")

# 4. Define a query
# Set up hashtags/keywords to search for tweets about the movie Wicked
query = "#Wicked -is:retweet lang:en"

# 5. Collect tweets and save them to a CSV file for analysis
def fetch_tweets(query, max_results=10):
    """
    Fetch tweets using the Twitter API with error handling for rate limits.
    """
    try:
        # Collect tweets
        tweets = client.search_recent_tweets(
            query=query,
            tweet_fields=["created_at", "author_id", "public_metrics", "text"],
            max_results=max_results
        )
        return tweets
    except TooManyRequests:
        print("Rate limit hit. Retrying in 15 minutes...")
        time.sleep(15 * 60)  # Wait for 15 minutes (rate limit reset)
        return fetch_tweets(query, max_results)  # Retry after waiting
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return None

# Fetch tweets
tweets = fetch_tweets(query, max_results=10)

# Process tweets if data is retrieved
if tweets and tweets.data:
    tweet_data = []
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
    csv_filename = "wicked_tweets.csv"
    df.to_csv(csv_filename, index=False)
    print(f"Tweets saved to {csv_filename}")
else:
    print("No tweets retrieved.")

# 6. Clean and process tweets (placeholder for further processing)
# Remove URLs, hashtags, mentions, and emojis

# Placeholder for sentiment analysis
# Perform sentiment analysis

# Placeholder for visualization
# Visualize and analyze
def check_rate_limit():
    try:
        rate_limit_status = client.get_rate_limit_status()
        search_status = rate_limit_status["resources"]["search"]["/search/tweets"]
        remaining = search_status["remaining"]
        reset_time = search_status["reset"]
        print(f"Remaining requests: {remaining}, Reset time: {reset_time}")
        return remaining, reset_time
    except Exception as e:
        print(f"Error checking rate limit: {e}")
        return 0, None
