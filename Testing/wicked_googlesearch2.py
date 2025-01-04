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

# Define search queries
queries = [
    "Wicked reviews", 
    "Wicked opinions", 
    "Wicked 2024 reactions", 
    "Wicked movie soundtrack", 
    "Cynthia Erivo in Wicked"
]

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
                all_data.append({
                    "query": query,
                    "title": item["title"],
                    "link": item["link"],
                    "snippet": item["snippet"]
                })
        else:
            break  # Stop if no more results

# Save Google Search results
if all_data:
    df = pd.DataFrame(all_data)
    df.to_csv("google_search_results_expanded.csv", index=False)
    print("Expanded search results saved to 'google_search_results_expanded.csv'")
else:
    print("No data fetched from Google Search.")

# ======================
# Optional Mock Data
# ======================
def create_mock_data():
    print("Creating mock data...")
    mock_data = [
        {"query": "Mock", "title": "Wicked review", "snippet": "Absolutely loved the visuals and music!", "sentiment": "positive"},
        {"query": "Mock", "title": "Wicked disappointment", "snippet": "The pacing was slow, and I expected more.", "sentiment": "negative"},
        {"query": "Mock", "title": "Wicked rocks!", "snippet": "The performances were outstanding!", "sentiment": "positive"}
    ]
    mock_df = pd.DataFrame(mock_data)
    mock_df.to_csv("mock_data.csv", index=False)
    print("Mock data saved to 'mock_data.csv'.")

# Uncomment this line to create mock data if needed
# create_mock_data()

# ======================
# Sentiment Analysis
# ======================
def perform_sentiment_analysis(file_name):
    print(f"Performing sentiment analysis on {file_name}...")
    data = pd.read_csv(file_name)
    if "snippet" in data.columns:
        # Add sentiment scores using TextBlob
        data["sentiment_score"] = data["snippet"].apply(lambda text: TextBlob(str(text)).sentiment.polarity)
        data["sentiment_label"] = data["sentiment_score"].apply(lambda score: "positive" if score > 0 else "negative" if score < 0 else "neutral")
        
        # Save sentiment analysis results
        output_file = file_name.replace(".csv", "_sentiment.csv")
        data.to_csv(output_file, index=False)
        print(f"Sentiment analysis results saved to '{output_file}'")
    else:
        print("No 'snippet' column found in the data. Skipping sentiment analysis.")

# Uncomment this line to perform sentiment analysis on the expanded search data
perform_sentiment_analysis("google_search_results_expanded.csv")

# ======================
# Visualization
# ======================
def visualize_domains(file_name):
    print(f"Visualizing domain data from {file_name}...")
    data = pd.read_csv(file_name)
    if "link" in data.columns:
        # Extract domains from links
        data["domain"] = data["link"].apply(lambda x: x.split("/")[2] if isinstance(x, str) else "unknown")
        
        # Count occurrences of each domain
        domain_counts = data["domain"].value_counts()
        
        # Plot the results
        domain_counts.plot(kind="bar", title="Domain Frequency", xlabel="Domain", ylabel="Count")
        print("Visualization completed.")
    else:
        print("No 'link' column found in the data. Skipping visualization.")

# Uncomment this line to visualize domain data
# visualize_domains("google_search_results_expanded.csv")
