import pandas as pd

data = {
    "StockA": [100, 102, 101, 105, 107, 110, 108, 111, 115, 117],
    "StockB": [50, 51, 53, 52, 56, 58, 57, 59, 60, 62]
}
# provide the indices to the dataframe
dates = pd.date_range(start="2023-01-01", periods=10, freq="D")
# now build the dataframe with data and its corresponding indices 
df = pd.DataFrame(data, index=dates)

# Your code starts here
# Calculate daily absolute returns
df["StockA_AbsReturn"] = df["StockA"].diff()
df["StockB_AbsReturn"] = df["StockB"].diff()

# Calculate daily percentage returns
df["StockA_PctReturn"] = df["StockA"].pct_change()*100
df["StockB_PctReturn"] = df["StockB"].pct_change()*100

# Identify the highest single-day percentage gain
stock_a_max = df["StockA_PctReturn"].idxmax()
stock_b_max = df["StockB_PctReturn"].idxmax()

stock_a_gain = df.loc[stock_a_max, 'StockA_PctReturn']
stock_b_gain = df.loc[stock_b_max, 'StockB_PctReturn']

if stock_a_gain > stock_b_gain:
    best_stock = "StockA"
    best_day = stock_a_max
    best_gain = stock_a_gain
else:
    best_stock = "StockB"
    best_day = stock_b_max
    best_gain = stock_b_gain

# Print the DataFrame with new columns
print(df)
# Print the result for the highest single-day percentage gain
print(f"\nThe highest single-day percentage gain was for {best_stock} on {best_day.date()} with a return of {best_gain:.2f}%")
