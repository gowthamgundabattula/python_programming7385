def analyze_travel_budget(expenses, exchange_rates, conversion_fee_pct, category_budgets):
    category_totals = {cat: 0.0 for cat in category_budgets}
    total_conversion_fees = 0.0
    processed_expenses = []

    # 1. Convert currencies and aggregate by category
    for exp in expenses:
        foreign_amount = exp["amount"]
        currency = exp["currency"]
        category = exp["category"]
        
        rate = exchange_rates.get(currency, 1.0)
        base_amount = foreign_amount * rate
        fee = base_amount * conversion_fee_pct
        
        total_expense = base_amount + fee
        total_conversion_fees += fee
        
        if category in category_totals:
            category_totals[category] += total_expense
        else:
            category_totals[category] = total_expense
            
        processed_expenses.append({
            "description": exp["desc"],
            "foreign": f"{foreign_amount} {currency}",
            "converted": total_expense
        })

    # 2. Identify the largest expense category
    largest_category = max(category_totals, key=category_totals.get)
    overall_spent = sum(category_totals.values())
    total_budget = sum(category_budgets.values())

    # 3. Generate Report Output
    print("=" * 65)
    print(f"{'MULTI-CURRENCY TRAVEL BUDGET ANALYSIS':^65}")
    print("=" * 65)
    print(f"{'Category':<18} | {'Budget ($)':<11} | {'Actual ($)':<11} | {'Status'}")
    print("-" * 65)
    
    for cat, budget in category_budgets.items():
        actual = category_totals[cat]
        diff = budget - actual
        status = f"Under (${abs(diff):.2f})" if diff >= 0 else f"⚠️ Over (${abs(diff):.2f})"
        print(f"{cat:<18} | ${budget:<10.2f} | ${actual:<10.2f} | {status}")
        
    print("-" * 65)
    print(f"Total Conversion Fees Paid : ${total_conversion_fees:.2f}")
    print(f"Total Spent vs Total Budget: ${overall_spent:.2f} / ${total_budget:.2f}")
    print(f"Largest Expense Category   : 🌟 {largest_category} (${category_totals[largest_category]:.2f})")
    print("=" * 65)


# --- Sample Execution ---
if __name__ == "__main__":
    # Exchange rates relative to USD (Base Currency)
    rates = {
        "USD": 1.0,
        "EUR": 1.08,
        "JPY": 0.0065,
        "GBP": 1.28
    }
    
    conversion_fee = 0.025  # 2.5% foreign transaction fee
    
    budgets = {
        "Accommodation": 1200.00,
        "Food & Dining": 500.00,
        "Transport": 400.00,
        "Sightseeing": 300.00
    }
    
    travel_expenses = [
        {"desc": "Hotel in Paris", "amount": 950.0, "currency": "EUR", "category": "Accommodation"},
        {"desc": "Bullet Train Ticket", "amount": 42000.0, "currency": "JPY", "category": "Transport"},
        {"desc": "Dinner in Tokyo", "amount": 12000.0, "currency": "JPY", "category": "Food & Dining"},
        {"desc": "Museum Pass", "amount": 150.0, "currency": "EUR", "category": "Sightseeing"},
        {"desc": "Taxi Rides", "amount": 180.0, "currency": "USD", "category": "Transport"},
        {"desc": "Cafe & Snacks", "amount": 90.0, "currency": "GBP", "category": "Food & Dining"}
    ]

    analyze_travel_budget(travel_expenses, rates, conversion_fee, budgets)
