"""Mobile Recharge Calculator
Scenario:
 A user recharges their mobile balance.
Task:
Take recharge amount
Add:
10% extra talktime if recharge ≥ 199
Show final balance
==================================================
"""
 # Take valid recharge amount
while True:
    amount = float(input("Enter recharge amount: "))
    if amount > 0:
        break
    else:
        print("Recharge amount must be greater than 0")

# Calculate bonus talktime
if amount >= 199:
    bonus = amount * 0.10
else:
    bonus = 0

# Final balance
final_balance = amount + bonus

# Display result
print("\n----- MOBILE RECHARGE DETAILS -----")
print("Recharge Amount:", amount)
print("Extra Talktime:", bonus)
print("Final Balance:", final_balance)
