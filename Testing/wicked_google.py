from pytrends.request import TrendReq
import pandas as pd

# Initialize pytrends
pytrends = TrendReq(hl="en-US", tz=360)

# Define search terms
keywords = ["Wicked"]

# Build payload
pytrends.build_payload(keywords, cat=0, timeframe="today 3-m", geo="", gprop="")

# Get interest over time
data = pytrends.interest_over_time()

# Save to CSV
if not data.empty:
    data.to_csv("google_trends_wicked.csv")
    print("Data saved to 'google_trends_wicked.csv'")
else:
    print("No data found.")
