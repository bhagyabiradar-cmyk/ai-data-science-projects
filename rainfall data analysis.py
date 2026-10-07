import numpy as np
import pandas as pd

# Rainfall data in mm
rainfall = np.array([45, 62, 78, 120, 150, 180, 210, 190, 140, 90, 55, 30])

# Create DataFrame
data = pd.DataFrame({
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    "Rainfall_mm": rainfall
})

# Calculate statistics
total_rainfall = np.sum(data["Rainfall_mm"])
average_rainfall = np.mean(data["Rainfall_mm"])
maximum_rainfall = np.max(data["Rainfall_mm"])
minimum_rainfall = np.min(data["Rainfall_mm"])

# Find months with highest and lowest rainfall
highest_month = data.loc[data["Rainfall_mm"].idxmax(), "Month"]
lowest_month = data.loc[data["Rainfall_mm"].idxmin(), "Month"]

# Display data
print("Rainfall Data:")
print(data)

print("\nTotal Rainfall:", total_rainfall, "mm")
print("Average Rainfall:", round(average_rainfall, 2), "mm")
print("Maximum Rainfall:", maximum_rainfall, "mm")
print("Minimum Rainfall:", minimum_rainfall, "mm")
print("Highest Rainfall Month:", highest_month)
print("Lowest Rainfall Month:", lowest_month)