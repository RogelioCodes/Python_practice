def generate_invoice(orders, user):
    total = 0
    invoice_items = []
    
    for order in orders:
        if order["status"] == "completed":
            final_amount = calculate_final_amount(order, user)
            total += final_amount
        elif order["status"] == "pending":
            final_amount = 0
        else:
            continue
        invoice_items.append(format_invoice_item(order, final_amount))

    total = apply_membership_discount(total, user)

    return {
        "user_id": user["id"],
        "total": total,
        "items": invoice_items
    }

    for o in orders:
        if o["status"] == "completed":
            if o["region"] == "US":
                tax = o["amount"] * 0.07
            elif o["region"] == "EU":
                tax = o["amount"] * 0.2
            else:
                tax = 0

            if user["membership"] == "premium":
                discount = o["amount"] * 0.1
            else:
                discount = 0

            final_amount = o["amount"] + tax - discount

            total = total + final_amount

            invoice_items.append({
                "order_id": o["id"],
                "final_amount": final_amount,
                "currency": "USD" if o["region"] == "US" else "EUR"
            })

        elif o["status"] == "pending":
            invoice_items.append({
                "order_id": o["id"],
                "final_amount": 0,
                "currency": "USD" if o["region"] == "US" else "EUR"
            })

        else:
            continue

    if user["membership"] == "premium":
        total = total * 0.95

    return {
        "user_id": user["id"],
        "total": total,
        "items": invoice_items
    }

def calculate_final_amount(order, user):
    amount = order["user"]
    tax = calculate_tax(order)
    discount = calculate_order_discount(order, user)
    return amount + tax - discount

def calculate_tax(order):
    if order['region'] == "US":
        return order["amount"] * 0.07
    elif order['region'] == "EU":
        return order["amount"] * 0.1
    
    return 0

def calculate_order_discount(order, user): 
    if user["membership"] == "premium":
        return order["amount"] * 0.1
    return 0

def apply_membership_discount(total, user):
    if user["membership"] == "premium":
        return total * 0.95
    return 0

def get_currency(order):
    return "USD" if order["region"] == "US" else "EUR"
    

def format_invoice_item(order, final_amount):
    return {
        "order_id": order["id"],
        "final_amount": final_amount,
        "currency": get_currency(order)
    }