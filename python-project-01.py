import pandas as pd

df = pd.read_csv("ecommerce_sales.csv")

# READING THE DATASET

print("First 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nTotal rows & columns:")
print(df.shape)

# DATA CLEANING

# Remove useless columns
if "Unnamed: 22" in df.columns:
    df.drop(columns=["Unnamed: 22"], inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fix the 'index' column if it's useless
if "index" in df.columns:
    df.drop(columns=["index"], inplace=True)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Fix numeric columns
df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce")
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

# Remove rows where Date or Amount is missing
df = df.dropna(subset=["Date", "Amount"])

# SIMPLE EDA

print("\nTotal Orders:", len(df))

print("\nTotal Sales Amount:")
print(df["Amount"].sum())

print("\nTotal Quantity Sold:")
print(df["Qty"].sum())

print("\nOrders by Status:")
print(df["Status"].value_counts())

print("\nOrders by Category:")
print(df["Category"].value_counts())

print("\nTop 5 Cities by Orders:")
print(df["ship-city"].value_counts().head())

print("\nB2B vs Non-B2B:")
print(df["B2B"].value_counts())

print("\nFulfillment Types:")
print(df["fulfilled-by"].value_counts())

print("\nSales by Country:")
print(df["ship-country"].value_counts())
