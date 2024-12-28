import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
bearer_token = os.getenv("BEARER_TOKEN")
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate to the Twitter API
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
    )

# Test authentication
try:
    user = client.get_me()
    print(f"Authenticated as @{user.data.username}")
except Exception as e:
    print(f"Authentication error: {e}")

# Define a query
# Set up hasthtags/ keywords to search for tweets about the movie Wicked (Example: #Wicked, #WickedMovie, #WickedMusical, #Elphaba, #Glinda)

# Collect tweets

# Clean and process tweets

# Perform sentiment analysis

# Visualize and analyze