import pandas as pd
import matplotlib.pyplot as plt

# Create temperature data
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"],
    "Temperature": [28, 30, 32, 29, 31, 33, 30]
}

df = pd.DataFrame(data)

print("Temperature Data:")
print(df)

# Average temperature
average = df["Temperature"].mean()
print("\nAverage Temperature:", average, "°C")

# Maximum temperature
maximum = df["Temperature"].max()
print("Maximum Temperature:", maximum, "°C")

# Minimum temperature
minimum = df["Temperature"].min()
print("Minimum Temperature:", minimum, "°C")

# Hottest day
hottest_day = df.loc[df["Temperature"].idxmax(), "Day"]
print("Hottest Day:", hottest_day)

# Coldest day
coldest_day = df.loc[df["Temperature"].idxmin(), "Day"]
print("Coldest Day:", coldest_day)

# Line chart
plt.plot(df["Day"], df["Temperature"], marker="o")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Weekly Temperature Analysis")
plt.xticks(rotation=45)
plt.show()