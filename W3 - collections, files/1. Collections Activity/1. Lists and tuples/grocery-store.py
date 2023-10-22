def display_product(product: dict):
    print(str(list(product.keys())[0]).ljust(30), product["expiration_date"])

def discount(product: dict, expiration_date: str) -> float:
    if expiration_date == "today":
        return round(product["price"] * 0.7, 2)
    else:
        return product["price"]

def display_product_with_price(product: dict):
    print(str(list(product.keys())[0]).ljust(30), product["expiration_date"].ljust(10), "£", product["price"])

products = [
{'milk': '1', 'expiration_date': 'today', 'price': 1.45},
{'organic milk': '2', 'expiration_date': 'tomorrow', 'price': 2.15},
{'filtered milk - whole': '3', 'expiration_date': 'tomorrow', 'price': 1.95},
{'filtered milk - skimmed': '4', 'expiration_date': 'today', 'price': 1.85}, 
]

# 1. Display each product alongside its expiration date.
for product in products:
    display_product(product)

# 2. Discount items expiring today by 30%
print(products)
for product in products:
    product["price"] = discount(product, product["expiration_date"])

# 3. Display items and their prices after discount.
for product in products:
    display_product_with_price(product)