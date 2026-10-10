import pandas as pd
import numpy as np

# Create expense dataset
data = {
    "Category": [
        "Food", "Travel", "Shopping", "Food",
        "Education", "Travel", "Entertainment",
        "Food", "Shopping", "Education"
    ],
    "Amount": [150, 80, 500, 200, 1000, 120, 300, 180, 700, 600]
}

df = pd.DataFrame(data)

# Calculate total expenses
total_expense = np.sum(df["Amount"])

# Calculate average expense
average_expense = np.mean(df["Amount"])

# Find highest expense
highest_expense = df.loc[df["Amount"].idxmax()]

# Find lowest expense
lowest_expense = df.loc[df["Amount"].idxmin()]

# Calculate category-wise expenses
category_expense = df.groupby("Category")["Amount"].sum()

# Display results
print("PERSONAL EXPENSE ANALYSIS")
print("-" * 35)

print("\nAll Expenses:")
print(df)

print("\nTotal Expense: ₹", total_expense)

print("Average Expense: ₹", round(average_expense, 2))

print("\nHighest Expense:")
print(highest_expense)

print("\nLowest Expense:")
print(lowest_expense)

print("\nCategory-wise Spending:")
print(category_expense)

print("\nMost Expensive Category:")
print(category_expense.idxmax())

print("\nTotal Number of Transactions:", len(df))

# Classify expenses
df["Expense_Type"] = np.where(
    df["Amount"] >= 500,
    "High Expense",
    "Normal Expense"
)

print("\nExpense Classification:")
print(df)