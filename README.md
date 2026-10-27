# Tourism Data Analysis and Travel Trend Visualization

## Problem Statement
Analyze tourism booking data to understand travel trends, seasonality, popular destinations and tourist spending behavior.

## Dataset
- Tourism_Raw.xlsx (raw data), Tourism_Cleaned_Preprocessed.xlsx (cleaned)
- Source: Synthetic dataset (6 months-3 years of bookings). Replace with a Kaggle tourism dataset if required.

## Steps Followed
1. Data loading and exploration (Pandas)
2. Cleaning: removed duplicates, invalid stay values, filled missing spend/rating
3. Analysis and visualization (Matplotlib, Seaborn)
4. Interactive dashboard (Streamlit)

## Key Findings
- Peak season: Oct-Dec and Apr-Jun
- Goa and Kerala are the most visited
- International tourists spend more per trip
- Spend correlates strongly with length of stay

## How to Run
Open notebook/tourism_analysis.ipynb in Google Colab, upload dataset/Tourism_Raw.xlsx and run all cells.
Dashboard: `cd dashboard && pip install -r requirements.txt && streamlit run app.py`

## Visualizations
See the visualizations/ folder.
