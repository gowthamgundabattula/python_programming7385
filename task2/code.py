def calculate_bill(units):
    """Calculates the progressive electricity bill based on slabs, fixed charges,

    surcharges, and rebates.
    """
    fixed_charge = 50.0
    surcharge_rate = 0.05  # 5% surcharge
    rebate = 15.0 if units <= 120 else 0.0  # Rebate for low usage

    energy_charge = 0.0
    if units <= 100:
        energy_charge = units * 3.50
    elif units <= 300:
        energy_charge = (100 * 3.50) + ((units - 100) * 5.00)
    else:
        energy_charge = (100 * 3.50) + (200 * 5.00) + ((units - 300) * 6.50)

    subtotal = energy_charge + fixed_charge
    surcharge = subtotal * surcharge_rate
    total_bill = subtotal + surcharge - rebate
    return round(total_bill, 2)


def analyze_electricity_bills(monthly_data):
    """Analyzes bills across multiple months and flags unusual increases."""
    prev_bill = None

    print(
        f"{'Month':<10} | {'Units':<8} | {'Bill ($)':<10} | {'Change (%)':<12} | {'Status'}"
    )
    print("-" * 65)

    for month, units in monthly_data.items():
        bill = calculate_bill(units)
        status = "Normal"
        pct_change = 0.0

        if prev_bill is not None and prev_bill > 0:
            pct_change = ((bill - prev_bill) / prev_bill) * 100
            if pct_change > 30.0:
                status = "⚠️ Unusual Increase"

        change_str = f"{pct_change:+.1f}%" if prev_bill is not None else "N/A"
        print(
            f"{month:<10} | {units:<8} | ${bill:<9.2f} | {change_str:<12} | {status}"
        )

        prev_bill = bill


# --- Sample Input ---
household_consumption = {
    "January": 110,
    "February": 105,
    "March": 240,
    "April": 430,  # Significant spike due to AC usage
    "May": 390,
}

if __name__ == "__main__":
    print("=== Progressive Electricity Billing & Trend Analysis ===")
    analyze_electricity_bills(household_consumption)
