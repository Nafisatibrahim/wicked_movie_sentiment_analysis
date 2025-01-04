import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key and Search Engine ID from environment variables
API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

# Define the search query
query = "Wicked movie"

# Construct the API URL
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"

# Make the API request
response = requests.get(url)
results = response.json()

# Process the results
data = []
if "items" in results:
    for item in results["items"]:
        data.append({
            "title": item["title"],
            "link": item["link"],
            "snippet": item["snippet"]
        })

    # Save the results to a CSV file
    df = pd.DataFrame(data)
    df.to_csv("google_search_results.csv", index=False)
    print("Search results saved to 'google_search_results.csv'")
else:
    print("No search results found.")
