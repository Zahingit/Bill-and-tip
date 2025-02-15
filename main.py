def calculate_tip():
    bill_amount = float(input("Enter the total bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage: $"))

    tip_amount = (tip_percentage / 100) * bill_amount
    total_amount = bill_amount + tip_amount

    print(f"\nTip Amount: ${tip_amount:.2f}")
    print(f"Total Amount (including tip): ${tip_amount:.2f}")
calculate_tip()