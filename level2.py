import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('railway_info_cleaned.csv')

# --- Task 2.1: Data Filtering ---

# Filter trains that operate on a specific day (e.g., Saturday)
saturday_trains = df[df['days'].str.lower() == 'saturday']
print("\n🔹 Trains that operate on Saturday:")
print(saturday_trains.head())

# Filter trains starting from a specific station (e.g., DELHI-SAFDAR JANG)
station_name = 'DELHI-SAFDAR JANG'
from_specific_station = df[df['Source_Station_Name'] == station_name]
print(f"\n🔹 Trains starting from {station_name}:")
print(from_specific_station.head())

# --- Task 2.2: Grouping and Aggregation ---

# Group by source station and count trains
train_count_by_source = df.groupby('Source_Station_Name')['Train_No'].count().sort_values(ascending=False)
print("\n🔹 Number of trains from each source station:")
print(train_count_by_source.head(10))

# Optional assumption: counting trains per day is not possible with only one 'days' column,
# but we can count how many trains operate on each day name
avg_trains_per_day = df['days'].value_counts()
print("\n🔹 Average number of trains per operating day:")
print(avg_trains_per_day)

# --- Task 2.3: Data Enrichment ---

# Categorize trains based on operating day
def categorize_day(day):
    day = day.lower()
    if day in ['saturday', 'sunday']:
        return 'Weekend'
    else:
        return 'Weekday'

df['Train_Type'] = df['days'].apply(categorize_day)

# Preview the new column
print("\n🔹 New column 'Train_Type' added (Weekday/Weekend):")
print(df[['Train_No', 'Train_Name', 'days', 'Train_Type']].head())

# Save the updated file
df.to_csv("railway_info_transformed.csv", index=False)
print("\n✅ Transformed data saved to 'railway_info_transformed.csv'")
