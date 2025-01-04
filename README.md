# Analyzing Public Sentiment Toward *Wicked* (2024) Movie Reviews

## Overview
This project focuses on analyzing public sentiment toward the 2024 movie *Wicked* using data collected from Google Search results. It includes data cleaning, preprocessing, visualizations, and sentiment analysis to uncover trends and insights from reviews.

![Wicked Movie](Images/wicked-cynthia-erivo-ariana-grande.webp)

---

## Features

### 1. Data Collection
- **Source**: Google Custom Search API.
- **Dataset**: Reviews scraped with queries categorized into various themes, including general reviews, audience reactions, and critical analysis.
- **Data Attributes**: 
  - `Query`: Search query used.
  - `Category`: Theme of the query (e.g., General Reviews, Audience Reactions).
  - `Title`: Title of the review/article.
  - `Link`: URL of the review/article.
  - `Snippet`: Short text snippet of the review.

### 2. Data Cleaning and Preprocessing
- Removed extra spaces, stopwords, and redundant text.
- Extracted and formatted review dates from snippets.
- Filtered reviews to include only those published after November 1, 2024.
- Normalized text to lowercase.

### 3. Data Analysis and Visualization
- **Categories Analysis**:
  - Bar chart showing the number of reviews by category.
- **Time-Based Trends**:
  - Line chart illustrating the number of reviews over time (weekly aggregation).
- **Common Words**:
  - Word cloud showcasing frequently used words in reviews.
- **Sentiment Analysis**:
  - Classified reviews into Positive, Neutral, and Negative sentiments.
  - Pie chart visualizing sentiment distribution.

### 4. Technologies Used
- **Languages**: Python
- **Libraries**:
  - Data Processing: `pandas`, `nltk`
  - Visualization: `matplotlib`, `wordcloud`
  - API Requests: `requests`
- **Google Custom Search API**: For fetching review data.
- **Jupyter Notebook**: Development and analysis environment.

---

## Installation

### Prerequisites
1. Python 3.x installed.
2. Required libraries:
   ```bash
   pip install pandas matplotlib wordcloud nltk
