
def process_orders(orders):
    total = 0
    processed_orders = []

    for order in orders:
        unit_price = apply_discount(order)
        final_price =  unit_price * order["quantity"]

        total += final_price
        processed_orders.append(format_order(order, final_price))
    

    return {"total": total, "orders": result}

'''
order =  {
    id,
    type,
    quantity,
    price
    
}
'''
def apply_discount(order):
    price = order["price"]
    quanity = order["quanitity"]

    if order["type"] == "A" and order["quantity"] > 10:
        order["price"] = price * 0.9 
    elif order["type"] == "B" and order["quantity"] > 5:
        order["price"] = price * 0.8
    
    return price

def format_order(order, final_price):
        return {
            "id": order["id"],
            "final_price": final_price,
            "type": order['type']
        }