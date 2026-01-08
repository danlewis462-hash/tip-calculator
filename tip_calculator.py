bill_amount = float(input("Enter total bill amount: ")) 
tax_percent = 8
tip_percent = 15

tax_amount = bill_amount * tax_percent / 100
subtotal = bill_amount + tax_amount
tip = subtotal * tip_percent / 100
subtotal = subtotal + tip
print(f"Tip amount: ${tip:.2f}")
print(f"Grand total: ${subtotal:.2f}")
