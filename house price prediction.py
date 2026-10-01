import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Create dataset
data = {
    "area": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3500],
    "bedrooms": [2, 2, 3, 3, 3, 4, 4, 4, 5, 5],
    "bathrooms": [1, 2, 2, 2, 3, 3, 3, 4, 4, 5],
    "price": [25, 30, 40, 48, 55, 65, 72, 82, 95, 110]
}

df = pd.DataFrame(data)

print("House Price Dataset:")
print(df)

# 2. Select input features and target
X = df[["area", "bedrooms", "bathrooms"]]
y = df["price"]

# 3. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create Linear Regression model
model = LinearRegression()

# 5. Train the model
model.fit(X_train, y_train)

# 6. Make predictions
y_pred = model.predict(X_test)

# 7. Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# 8. Predict price for a new house
new_house = pd.DataFrame({
    "area": [1600],
    "bedrooms": [3],
    "bathrooms": [2]
})

predicted_price = model.predict(new_house)

print("\nNew House Details:")
print(new_house)

print(
    "\nPredicted House Price:",
    round(predicted_price[0], 2),
    "Lakhs"
)