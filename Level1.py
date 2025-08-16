import pandas as pd

# Load the dataset
df = pd.read_csv('Railway_info.csv')

# Show first 10 rows
print("\n🔹 First 10 Rows:")
print(df.head(10))

# Show structure
print("\n🔹 Data Types and Non-Null Counts:")
print(df.info())

# Show missing values
print("\n🔹 Missing Values per Column:")
print(df.isnull().sum())

# Total trains
print(f"\n🔹 Total trains: {df.shape[0]}")

# Unique source and destination stations
print(f"🔹 Unique source stations: {df['Source_Station_Name'].nunique()}")
print(f"🔹 Unique destination stations: {df['Destination_Station_Name'].nunique()}")

# Most common source and destination
print(f"🔹 Most common source: {df['Source_Station_Name'].mode()[0]}")
print(f"🔹 Most common destination: {df['Destination_Station_Name'].mode()[0]}")

# Handle missing values (if any)
df.fillna("Unknown", inplace=True)

# Standardize station names to uppercase
df['Source_Station_Name'] = df['Source_Station_Name'].str.upper()
df['Destination_Station_Name'] = df['Destination_Station_Name'].str.upper()

# Save cleaned data
df.to_csv("railway_info_cleaned.csv", index=False)
print("\n✅ Cleaned data saved to 'railway_info_cleaned.csv'")

