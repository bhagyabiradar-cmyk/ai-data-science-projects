import pandas as pd
import matplotlib.pyplot as plt

# Customer purchase data
data = {
    "Customer": ["Asha", "Ravi", "Priya", "Rahul", "Sneha", "Arun", "Meena", "Kiran"],
    "Product": ["Laptop", "Phone", "Laptop", "Headphones",
                "Phone", "Laptop", "Tablet", "Phone"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories",
                 "Electronics", "Electronics", "Electronics", "Electronics"],
    "Quantity": [1, 2, 1, 3, 1, 2, 1, 2],
    "Price": [60000, 25000, 60000, 2000, 25000, 60000, 30000, 25000]
}

df = pd.DataFrame(data)

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("CUSTOMER SALES DATA")
print(df)

# Total sales
total_sales = df["Total_Sales"].sum()

print("\nTotal Sales:", total_sales)

# Sales by product
product_sales = df.groupby("Product")["Total_Sales"].sum()

print("\nSales by Product:")
print(product_sales)

# Best-selling product
best_product = product_sales.idxmax()

print("\nBest-Selling Product:", best_product)

# Highest quantity sold
quantity = df.groupby("Product")["Quantity"].sum()

print("\nQuantity Sold:")
print(quantity)

# Visualization
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.show()