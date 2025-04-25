'''
Problem: Inventory Matching and Pricing

Description:
Develop a program that checks if an order can be fulfilled based on available inventory and budget constraints.
The program should:
1. Match order items with inventory items
2. Check if there is sufficient stock for each item
3. Calculate the total cost of the order
4. Determine if the order can be fulfilled within the given budget

This problem simulates real-world inventory management and order processing systems.

Approach:
- Sort inventory items by price to prioritize cheaper items
- Check each order item against the inventory
- Track total cost as items are processed
- Validate against stock availability and budget constraints
- Provide detailed feedback on order fulfillment status
'''

def check_order_fulfillment(inventory, order, budget):
    total_cost = 0
    fulfillable = True

    # Sort items based on price (lowest to highest) to prioritize cheaper items
    sorted_inventory = sorted(inventory, key=lambda x: x["price"])

    for item in order:
        # Find the corresponding item in the inventory
        for product in sorted_inventory:
            if product["name"] == item["name"]:
                # Check if the inventory has enough stock
                if product["quantity"] >= item["quantity"]:
                    total_cost += item["quantity"] * product["price"]
                    product["quantity"] -= item["quantity"]
                    break
                else:
                    print(f"Insufficient stock for {item['name']}.")
                    fulfillable = False
                    break
        else:
            print(f"Item {item['name']} not found in inventory.")
            fulfillable = False
            break

    if fulfillable:
        if total_cost <= budget:
            print(f"Order can be fulfilled. Total cost: ₹{total_cost}")
        else:
            print(f"Order cannot be fulfilled. Total cost ₹{total_cost} exceeds budget of ₹{budget}.")
    else:
        print("Order is partially fulfillable or impossible.")

# Example usage
if __name__ == "__main__":
    # Example inventory and order
    inventory = [
        {"name": "Laptop", "quantity": 5, "price": 30000},
        {"name": "Smartphone", "quantity": 10, "price": 15000},
        {"name": "Headphones", "quantity": 15, "price": 5000}
    ]

    order = [
        {"name": "Laptop", "quantity": 2},
        {"name": "Smartphone", "quantity": 3}
    ]

    budget = 80000

    check_order_fulfillment(inventory, order, budget)