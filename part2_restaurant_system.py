menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

print("\n--- TASK 1: MENU EXPLORATION ---")

categories = set(item["category"] for item in menu.values())
for category in categories:
    print(f"\n===== {category} =====")
for item_name, details in menu.items():
        if details["category"] == category:
            
            price = details["price"]
            availability = "Available" if details["available"] else "Unavailable"
            
            print(f"{item_name:<15} ₹{price:.2f}   [{availability}]")
            total_items = len(menu)
print("\nTotal items on menu:", total_items)
available_items = sum(1 for item in menu.values() if item["available"])
print("Available items:", available_items)
most_expensive = max(menu.items(), key=lambda x: x[1]["price"])

print("Most expensive item:", most_expensive[0], "-", most_expensive[1]["price"])
print("\nItems under ₹150:")

for item_name, details in menu.items():
    if details["price"] < 150:
        print(item_name, "-", details["price"])

print("\n--- TASK 2: INVENTORY STATUS ---")

for item, details in inventory.items():
    stock = details["stock"]
    reorder = details["reorder_level"]

    if stock <= reorder:
        print(f"{item} → LOW STOCK (Stock: {stock})")
    else:
        print(f"{item} → In Stock (Stock: {stock})")

print("\nUnavailable Items:")

for item, details in menu.items():
    if not details["available"]:
        print(item)

print("\nItems to Reorder:")

for item, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(item)

print("\n--- TASK 3: ORDER SYSTEM ---")

order = []

while True:
    item = input("Enter item name (or type 'done' to finish): ")

    if item.lower() == "done":
        break

    order.append(item)
total_bill = 0

print("\nOrder Summary:")

for item in order:
    # Check if item exists
    if item not in menu:
        print(f"{item} → Not on menu")
        continue

    # Check availability
    if not menu[item]["available"]:
        print(f"{item} → Not available")
        continue

    # Check stock
    if inventory[item]["stock"] <= 0:
        print(f"{item} → Out of stock")
        continue

    # Valid item → process
    price = menu[item]["price"]
    total_bill += price

    # Reduce stock
    inventory[item]["stock"] -= 1

    print(f"{item} → Added (₹{price})")

print("\nTotal Bill: ₹", total_bill)

print("\n--- TASK 4: SALES ANALYSIS ---")

total_revenue = 0
total_orders = 0
item_count = {}

for date, orders in sales_log.items():
    for order in orders:
        total_revenue += order["total"]
        total_orders += 1

for item in order["items"]:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

best_item = max(item_count, key=item_count.get)

print("Total Revenue: ₹", total_revenue)
print("Total Orders:", total_orders)
print("Best Selling Item:", best_item, "-", item_count[best_item], "times")


