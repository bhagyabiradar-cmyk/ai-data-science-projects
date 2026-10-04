sales = {
    "Laptop": 25,
    "Mobile": 40,
    "Tablet": 18,
    "Headphones": 32,
    "Keyboard": 15
}

highest_product = max(sales, key=sales.get)

print("Sales Data:")
for product, quantity in sales.items():
    print(product, ":", quantity)

print("\nHighest Selling Product:", highest_product)
print("Units Sold:", sales[highest_product])