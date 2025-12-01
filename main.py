# Weather Data Analysis Project

# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
data = pd.read_csv("weather.csv")

# Display first few rows
print("\n--- WEATHER DATA SAMPLE ---")
print(data.head())

# Basic info
print("\n--- DATA INFO ---")
print(data.info())

# Summary statistics
print("\n--- SUMMARY STATISTICS ---")
print(data.describe())

# Check for missing values
print("\n--- MISSING VALUES ---")
print(data.isnull().sum())

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Extract useful time features
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day_name()

# 1 Average temperature, humidity, and wind speed
print("\n--- AVERAGE VALUES ---")
print("Average Temperature:", round(data['Temperature'].mean(), 2))
print("Average Humidity:", round(data['Humidity'].mean(), 2))
print("Average Wind Speed:", round(data['WindSpeed'].mean(), 2))

# 2 Visualize Temperature Trend Over Time
plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Temperature'], marker='o')
plt.title('Temperature Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid()
plt.show()

# 3 Compare Weather Types
plt.figure(figsize=(8,5))
sns.countplot(x='Weather', data=data, palette='viridis')
plt.title('Count of Different Weather Types')
plt.show()

# 4 Correlation Heatmap
plt.figure(figsize=(8,5))
sns.heatmap(data[['Temperature','Humidity','WindSpeed']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Weather Variables')
plt.show()

# 5 Monthly Average Temperature
monthly_avg = data.groupby('Month')['Temperature'].mean()
plt.figure(figsize=(8,5))
monthly_avg.plot(kind='bar')
plt.title('Average Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.show()

print("\n Weather Data Analysis Completed Successfully!")
