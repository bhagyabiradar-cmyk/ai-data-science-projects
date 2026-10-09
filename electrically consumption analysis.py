import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create electricity consumption data
data = {
    "Day": ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"],
    "Units": [12, 15, 10, 18, 20, 25, 16]
}

df = pd.DataFrame(data)

# Display the dataset
print("Electricity Consumption Data:")
print(df)

# Calculate statistics using NumPy
average = np.mean(df["Units"])
maximum = np.max(df["Units"])
minimum = np.min(df["Units"])

print("\nAverage Consumption:", average)
print("Maximum Consumption:", maximum)
print("Minimum Consumption:", minimum)

# Find the day with the highest consumption
highest_day = df.loc[df["Units"].idxmax(), "Day"]

print("Day with Highest Consumption:", highest_day)

# Visualize the data
plt.bar(df["Day"], df["Units"])

plt.title("Weekly Electricity Consumption")
plt.xlabel("Day")
plt.ylabel("Units Consumed")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()