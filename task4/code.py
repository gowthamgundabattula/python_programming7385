def generate_invoice(cart_items):
    # Category tax rates dictionary
    tax_rates = {
        "Electronics": 0.18,
        "Clothing": 0.05,
        "Groceries": 0.00,
        "Default": 0.10
    }
    
    subtotal = 0.0
    total_tax = 0.0
    itemized_details = []
    
    # Process each item in the cart
    for item in cart_items:
        name = item["name"]
        category = item.get("category", "Default")
        price = item["price"]
        qty = item["qty"]
        
        item_subtotal = price * qty
        tax_rate = tax_rates.get(category, tax_rates["Default"])
        item_tax = item_subtotal * tax_rate
        
        subtotal += item_subtotal
        total_tax += item_tax
        
        itemized_details.append({
            "name": name,
            "qty": qty,
            "price": price,
            "subtotal": item_subtotal,
            "tax": item_tax
        })
        
    # Threshold discount rules based on subtotal
    discount = 0.0
    if subtotal > 500:
        discount = subtotal * 0.12  # 12% discount for orders > $500
    elif subtotal > 200:
        discount = subtotal * 0.05  # 5% discount for orders > $200
        
    # Maximum concession limit cap
    max_concession = 75.00
    if discount > max_concession:
        discount = max_concession
        
    final_total = subtotal + total_tax - discount
    
    # Print Itemized Invoice
    print("=" * 65)
    print(f"{'RETAIL INVOICE RECEIPT':^65}")
    print("=" * 65)
    print(f"{'Item Name':<20} | {'Qty':<4} | {'Price':<7} | {'Subtotal':<9} | {'Tax':<7}")
    print("-" * 65)
    for it in itemized_details:
        print(f"{it['name']:<20} | {it['qty']:<4} | ${it['price']:<6.2f} | ${it['subtotal']:<8.2f} | ${it['tax']:<6.2f}")
    print("-" * 65)
    print(f"{'Gross Subtotal:':<45} ${subtotal:>15.2f}")
    print(f"{'Total Tax:':<45} ${total_tax:>15.2f}")
    print(f"{'Discount Applied (Capped at Max):':<45} -${discount:>14.2f}")
    print("=" * 65)
    print(f"{'FINAL TOTAL PAYABLE:':<45} ${final_total:>15.2f}")
    print("=" * 65)


# --- Sample Execution ---
if __name__ == "__main__":
    cart = [
        {"name": "Wireless Mouse", "category": "Electronics", "price": 45.00, "qty": 2},
        {"name": "Cotton T-Shirt", "category": "Clothing", "price": 20.00, "qty": 3},
        {"name": "Organic Rice (5kg)", "category": "Groceries", "price": 25.00, "qty": 2},
        {"name": "Bluetooth Speaker", "category": "Electronics", "price": 120.00, "qty": 1}
    ]
    generate_invoice(cart)
