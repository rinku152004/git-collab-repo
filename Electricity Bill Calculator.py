"""Electricity Bill Calculator
Scenario:
 Calculate monthly electricity bill.
Task:
Take units consumed
Charges:
First 100 units → ₹3/unit
Next 100 units → ₹5/unit
Above 200 units → ₹7/unit
Print total bill
============================================
"""
# Take units consumed
while True:
    units = int(input("Enter units consumed: "))
    if units >= 0:
        break
    else:
        print("Enter units greater than zero. Try again.")


bill = 0

if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = (100 * 3) + ((units - 100) * 5)
else:
    bill = (100 * 3) + (100 * 5) + ((units - 200) * 7)

# Display total bill
print("\n----- ELECTRICITY BILL -----")
print("Units Consumed:", units)
print("Total Bill Amount: ₹", bill)

    
