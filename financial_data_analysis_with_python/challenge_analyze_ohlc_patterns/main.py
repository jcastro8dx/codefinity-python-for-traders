import pandas as pd

# Create a DataFrame with OHLC data for 7 consecutive days
# Fill in the data below as required by the instructions
data = {
    "Date": [
        "2024-06-01",
        "2024-06-02",
        "2024-06-03",
        "2024-06-04",
        "2024-06-05",
        "2024-06-06",
        "2024-06-07"
    ],
    "Open":  [100, 102, 101, 103, 104, 105, 104],
    "High":  [103, 104, 103, 105, 106, 107, 106],
    "Low":   [99, 101, 100, 102, 103, 104, 103],
    "Close": [102, 103, 102, 104, 105, 106, 105]
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# Calculate daily range (High - Low) and add as a new column
df["Range"] = df["High"] - df["Low"]
# Now add this new column to the DataFrame
df = df.add_column[df["Range"]] ?????

# Identify days where Close > Open and Close > previous day's Close
mask = (df["Close"] > df["Open"]) & (df["Close"] > df["Prev_Close"])

# Output the list of dates (YYYY-MM-DD format) that match the pattern
bullish_days = df[mask].index.strftime("%Y-%m-%d").tolist()
print(bullish_days)
