import pandas as pd

data = {
    "Date": [
        "2024-01-01", "2024-01-02", "2024-01-03",
        "2024-01-04", "2024-01-05", "2024-01-06",
        "2024-01-07"
    ],
    "Close": [
        101.5, None, 102.7, None, 104.2, 105.0, None
    ]
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

print("Missing values per day:")
print(df.isnull())

# Fill missing values using linear interpolation
cleaned_df = df.interpolate(method="linear")

print("\nCleaned closing prices (after interpolation):")
# print(cleaned_df)
print(cleaned_df)

mean_price = cleaned_df["Close"].mean()
std_price = cleaned_df["Close"].std()

print("\nMean closing price:", mean_price)
print("Standard deviation of closing price:", std_price)
