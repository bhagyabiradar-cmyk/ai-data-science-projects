import pandas as pd
import matplotlib.pyplot as plt

# Sales dataset
data = {
    "Product": [
        "Laptop", "Phone", "Laptop", "Headphones",
        "Phone", "Tablet", "Laptop", "Phone"
    ],
    "Category": [
        "Electronics", "Electronics", "Electronics", "Accessories",
        "Electronics", "Electronics", "Electronics", "Electronics"
    ],
    "Quantity": [1, 2, 1, 3, 2, 1, 2, 1],
    "Price": [60000, 25000, 60000, 2000, 25000, 30000, 60000, 25000]
}

df = pd.DataFrame(data)

# Calculate sales amount
df["Sales"] = df["Quantity"] * df["Price"]

print("SALES DATA")
print(df)

# 1. Total sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# 2. Total quantity
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)

# 3. Average order value
average_sales = df["Sales"].mean()
print("Average Order Value:", round(average_sales, 2))

# 4. Sales by product
product_sales = df.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(product_sales)

# 5. Best-selling product
best_product = product_sales.idxmax()

print("\nBest-Selling Product:", best_product)

# 6. Quantity by product
product_quantity = df.groupby("Product")["Quantity"].sum()

print("\nQuantity Sold by Product:")
print(product_quantity)

# 7. Visualization
product_sales.sort_values().plot(kind="barh")

plt.title("Sales by Product")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.show()