import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the transformed data
df = pd.read_csv("railway_info_transformed.csv")

# Create plots directory if not exists
os.makedirs("plots", exist_ok=True)

# --- Task 3.1: Pattern Analysis ---

# Count how many trains operate on each day
day_counts = df['days'].value_counts().sort_index()

# Bar chart: Number of trains per day
plt.figure(figsize=(8, 4))
sns.barplot(x=day_counts.index, y=day_counts.values, palette="Set2")
plt.title("Trains Operating Per Day")
plt.xlabel("Day")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/trains_per_day.png")
print("\n✅ Saved: plots/trains_per_day.png")

# Top 10 Source stations by frequency
top_sources = df['Source_Station_Name'].value_counts().head(10)

# Bar chart: Top 10 Source Stations
plt.figure(figsize=(10, 5))
sns.barplot(x=top_sources.values, y=top_sources.index, palette="Set3")
plt.title("Top 10 Source Stations by Train Count")
plt.xlabel("Number of Trains")
plt.ylabel("Source Station")
plt.tight_layout()
plt.savefig("plots/top_source_stations.png")
print("✅ Saved: plots/top_source_stations.png")

# --- Task 3.2: Correlation and Insights ---

# Count of Weekday vs Weekend trains
train_type_counts = df['Train_Type'].value_counts()

# Bar chart: Weekday vs Weekend
plt.figure(figsize=(6, 4))
sns.barplot(x=train_type_counts.index, y=train_type_counts.values, palette="Set1")
plt.title("Weekday vs Weekend Trains")
plt.xlabel("Train Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("plots/train_type_distribution.png")
print("✅ Saved: plots/train_type_distribution.png")

# Print numerical insights
print("\n🔹 Trains operating each day:\n", day_counts)
print("\n🔹 Train types (Weekday/Weekend):\n", train_type_counts)
