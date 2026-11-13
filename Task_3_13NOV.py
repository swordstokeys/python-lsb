# Sample E-commerce Inventory Database

inventory = {

    "SKU_101": {"name": "Wireless Mouse", "price": 25.00, "stock_count": 50, "category": "Electronics"},

    "SKU_102": {"name": "Gaming Keyboard", "price": 80.00, "stock_count": 0, "category": "Electronics"},

    "SKU_103": {"name": "Yoga Mat", "price": 30.00, "stock_count": 15, "category": "Fitness"},

    "SKU_104": {"name": "Bluetooth Speaker", "price": 120.00, "stock_count": 5, "category": "Electronics"},

    "SKU_105": {"name": "Protein Shaker", "price": 15.00, "stock_count": 0, "category": "Fitness"},

}
# UPDATE (Flash Sale):  #    Apply a 15% discount to the 'price' of every item in the "Electronics" category.
# LOGIC (Restock Alert):  #    Loop through the inventory. If 'stock_count' is 0, add a new key  #    called 'restock_urgent' with the value True.
# SAFE ACCESS (Data Integrity):  #    Check for a 'last_sold' key. If it doesn't exist, use .setdefault()  #    to set it to "Never".
# VIEW: Print the final updated inventory.





# function 1 Check if it's electronic then apply discount 
discount = 0.15

def flash_sale(inventory: dict, discount: float) -> dict:
    for item in inventory.values():
        if item["category"] == "Electronics":
            item["price"] = item["price"] * (1 - discount)

    return inventory


# function 2 if stocke goes below 1 ( haha Zero ) then show restock warning 

def restock_alert(inventory: dict) -> dict:
    for item in inventory.values():
        if item["stock_count"] == 0:
            item["restock_urgent"] = True

    return inventory




flash_sale(inventory, discount)
restock_alert(inventory)


for sku, item in inventory.items():
    print(sku, item)






















