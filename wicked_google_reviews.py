import requests
import pandas as pd
import os
from dotenv import load_dotenv
from textblob import TextBlob

# Load environment variables
load_dotenv()

# Get API Key and Search Engine ID from environment variables
API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

# Define query categories
query_categories = {
    "General Reviews": [
        "Wicked movie reviews", "Wicked 2024 reviews", "Is Wicked a good movie?",
        "Critics review Wicked 2024", "Audience reaction to Wicked"
    ],
    "Social Media Reactions": [
        "Twitter reactions to Wicked movie", "What people are saying about Wicked 2024",
        "Reddit Wicked movie discussion", "Social media reactions to Wicked"
    ],
    "Comparison and Opinions": [
        "Wicked vs other musicals", "How does Wicked compare to other movies?",
        "Best moments in Wicked 2024", "Cynthia Erivo performance in Wicked",
        "Ariana Grande Glinda reviews"
    ],
    "Performance and Cast": [
        "Cynthia Erivo as Elphaba", "Ariana Grande as Glinda", "Wicked cast performances",
        "Songs in Wicked 2024", "Wicked soundtrack reviews"
    ],
    "Audience Reactions": [
        "Wicked movie theater reactions", "Wicked 2024 audience reviews",
        "People's thoughts on Wicked movie", "Fans review Wicked"
    ],
    "Critical Analysis": [
        "Metacritic reviews for Wicked", "Rotten Tomatoes Wicked reviews",
        "Wicked movie box office analysis", "Wicked 2024 movie ratings"
    ],
    "Related Topics": [
        "Wicked musical vs movie", "Behind the scenes of Wicked movie",
        "Interviews with the cast of Wicked", "Wicked director Jon M. Chu reviews"
    ],
    "International Reactions": [
        "Global reaction to Wicked movie", "Wicked reviews UK", "Wicked reviews US",
        "Wicked reviews Australia", "Wicked reviews in Asia"
    ],
    "Negative Comments": [
        "Criticism of Wicked movie", "What people didn't like about Wicked",
        "Is Wicked movie overhyped?", "Worst parts of Wicked movie"
    ],
    "Song and Soundtrack Reviews": [
        "Best songs in Wicked 2024", "Wicked soundtrack reviews",
        "Elphaba's song in Wicked", "Glinda's song in Wicked"
    ]
}

# Combine all queries into one list
queries = [query for category in query_categories.values() for query in category]

# Initialize a list to store all search results
all_data = []

# Fetch Google Search results with pagination
for query in queries:
    print(f"Fetching results for query: {query}")
    for start_index in range(1, 51, 10):  # Fetch up to 50 results (5 pages)
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start_index}"
        response = requests.get(url)
        results = response.json()
        
        if "items" in results:
            for item in results["items"]:
                # Determine category for the query
                category = next((cat for cat, qs in query_categories.items() if query in qs), "Unknown")
                all_data.append({
                    "query": query,
                    "category": category,
                    "title": item["title"],
                    "link": item["link"],
                    "snippet": item["snippet"]
                })
        else:
            break  # Stop if no more results

# Save Google Search results
if all_data:
    df = pd.DataFrame(all_data)
    df.to_csv("Output/google_search_results_with_categories.csv", index=False)
    print("Search results saved to 'google_search_results_with_categories.csv'")
else:
    print("No data fetched from Google Search.")