def payment_for_order(total_cost,user_name):
    payment_type = {
        "DEBIT_CARD",
        "CREDIT_CARD",
        "PAY_BY_CASH"
    }
    print(" "*10, "Available Payment Modes")
    for p in payment_type:
        print(p)
    payment_choice = input(f"What kind of payment do you like to do {user_name}?")
    if payment_choice in payment_type:
        print(f"Amount to be paid ${total_cost} through {payment_choice}")


