import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 65, 70, 75, 85]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Input and output
X = df[["Study_Hours"]]
y = df["Marks"]

# Create AI/ML model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict marks for 6.5 study hours
prediction = model.predict([[6.5]])

print("\nPredicted Marks:", round(prediction[0], 2))