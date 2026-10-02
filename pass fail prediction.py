import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Student dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [55, 60, 65, 70, 75, 80, 85, 90],
    "Result": ["Fail", "Fail", "Fail", "Pass",
               "Pass", "Pass", "Pass", "Pass"]
}

df = pd.DataFrame(data)

# Features
X = df[["Study_Hours", "Attendance"]]

# Target
y = df["Result"]

# Create AI model
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# New student's details
new_student = [[5, 78]]

# Prediction
prediction = model.predict(new_student)

print("Predicted Result:", prediction[0])