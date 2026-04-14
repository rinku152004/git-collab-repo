"""Shop Bill Calculator
Scenario:
 A small shop wants to calculate the total bill.
Task:
Take price of 3 items
Calculate:
Total amount
5% discount if total > 1000
Final payable amount
========================================================
"""
# Take price of 3 items
item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

# Calculate total amount
total = item1 + item2 + item3

# Calculate discount
if total > 1000:
    discount = total * 0.05   # 5% discount
else:
    discount = 0

# Final payable amount
final_amount = total - discount

# Display bill
print("\n----- SHOP BILL -----")
print("Total Amount:", total)
print("Discount:", discount)
print("Final Payable Amount:", final_amount)
