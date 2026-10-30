def calculate_passenger_fare(passenger):
    name = passenger["name"]
    age = passenger["age"]
    travel_class = passenger["class"]  # "Sleeper", "AC3", "AC2"
    distance = passenger["distance"]
    is_cancelled = passenger["cancelled"]

    # 1. Base fare calculation using distance slabs and class multipliers
    rate_per_km = 1.25
    class_multipliers = {"Sleeper": 1.0, "AC3": 1.6, "AC2": 2.2}
    multiplier = class_multipliers.get(travel_class, 1.0)

    base_fare = distance * rate_per_km * multiplier

    # 2. Age-based concessions
    concession_label = "Standard"
    discount_pct = 0.0

    if age < 5:
        discount_pct = 1.0  # Free for infants
        concession_label = "Infant (100% Off)"
    elif 5 <= age <= 12:
        discount_pct = 0.50  # 50% off for children
        concession_label = "Child (50% Off)"
    elif age >= 60:
        discount_pct = 0.40  # 40% off for senior citizens
        concession_label = "Senior Citizen (40% Off)"

    discounted_fare = base_fare * (1.0 - discount_pct)

    # 3. Reservation Fee
    reservation_fee = 30.0 if discount_pct < 1.0 else 0.0

    # 4. Cancellation & Refund logic
    total_amount = discounted_fare + reservation_fee
    penalty = 0.0
    refund = 0.0

    if is_cancelled:
        penalty = max(50.0, discounted_fare * 0.20)  # 20% penalty or min $50
        refund = max(0.0, total_amount - penalty)
        status = "CANCELLED"
    else:
        status = "CONFIRMED"

    return {
        "name": name,
        "age": age,
        "class": travel_class,
        "distance": distance,
        "base_fare": base_fare,
        "concession": concession_label,
        "reservation_fee": reservation_fee,
        "total": total_amount,
        "status": status,
        "penalty": penalty,
        "refund": refund,
    }


def generate_reservation_report(passengers):
    print("=" * 75)
    print(f"{'RAILWAY FARE & RESERVATION STATEMENT':^75}")
    print("=" * 75)

    for p in passengers:
        res = calculate_passenger_fare(p)
        print(f"Passenger Name : {res['name']} (Age: {res['age']})")
        print(f"Travel Class   : {res['class']} | Distance: {res['distance']} km")
        print(f"Concession     : {res['concession']}")
        print(f"Base Fare      : ${res['base_fare']:.2f} | Reservation Fee: ${res['reservation_fee']:.2f}")
        print(f"Status         : {res['status']}")

        if res["status"] == "CANCELLED":
            print(f"Cancellation Penalty: ${res['penalty']:.2f} | Refund Amount: ${res['refund']:.2f}")
        else:
            print(f"Final Payable  : ${res['total']:.2f}")
        print("-" * 75)


# --- Sample Input ---
if __name__ == "__main__":
    passenger_list = [
        {"name": "Robert Smith", "age": 45, "class": "AC3", "distance": 650, "cancelled": False},
        {"name": "Margaret Smith", "age": 62, "class": "AC3", "distance": 650, "cancelled": False},
        {"name": "Tommy Smith", "age": 8, "class": "Sleeper", "distance": 650, "cancelled": False},
        {"name": "David Clark", "age": 30, "class": "AC2", "distance": 1200, "cancelled": True},
    ]

    generate_reservation_report(passenger_list)
