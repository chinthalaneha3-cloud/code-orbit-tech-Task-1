import pandas as pd

data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1005],
    "Date": ["2026-08-01", "2026-08-02", "2026-08-03",
             "2026-08-04", "2026-08-05", "2026-08-05"],
    "Product": ["Laptop", " Mouse ", "Keyboard", "Monitor", "Chair", "Chair"],
    "Category": ["Electronics", "electronics", "Electronics",
                 "Electronics", "Furniture", "Furniture"],
    "Region": ["South", "South", "North", "East", "west", "west"],
    "Quantity": [2, 5, 3, 2, 4, 4],
    "Unit_Price": [55000, 750, 1800, 12000, 7000, 7000]
}

df = pd.DataFrame(data)

# Remove duplicates
df = df.drop_duplicates()

# Clean text
df["Product"] = df["Product"].str.strip().str.title()
df["Category"] = df["Category"].str.strip().str.title()
df["Region"] = df["Region"].str.strip().str.title()

# Convert data types
df["Date"] = pd.to_datetime(df["Date"])
df["Quantity"] = pd.to_numeric(df["Quantity"])
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"])

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Show cleaned data
print("CLEANED DATA")
print(df)

# Save as CSV
df.to_csv(
    "/storage/emulated/0/Download/cleaned_sales_data.csv",
    index=False
)

print("\nDATA CLEANING COMPLETED!")
print("File saved: Download/cleaned_sales_data.csv")