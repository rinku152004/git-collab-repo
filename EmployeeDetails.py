"""1Create a small program that stores and displays employee details using proper data types.
Requirements:
• Store employee information such as:
Employee ID
Employee Name
Age
Department
Salary
Is Employee Permanent (Yes/No)
• Use appropriate data types for each value.
• Display the stored data in a clean and readable format.

====================================================================
"""
n = int(input("How many employee details you want to display: "))

employees = []

# Function to take only alphabet input (spaces allowed)
def alpha_input(prompt):
    while True:
        value = input(prompt).strip()
        if value.replace(" ", "").isalpha():
            return value
        else:
            print("Only alphabets are allowed. Try again.")

for i in range(n):
    print(f"\n==== Enter details of employee {i + 1} ====")
    
    emp_id = int(input("Enter id of an employee: "))
    
    name = alpha_input("Enter name of an employee: ")
    
    age = int(input("Enter age of an employee: "))
    
    dept = alpha_input("Enter department name of an employee: ")
    
    sal = int(input("Enter salary of an employee: "))

    while True:
        ans = input("Is employee permanent? (yes/no): ").lower()
        if ans == "yes":
            prmt = True
            break
        elif ans == "no":
            prmt = False
            break
        else:
            print("Invalid input! Enter yes or no.")

    employees.append({
        "id": emp_id,
        "name": name,
        "age": age,
        "dept": dept,
        "salary": sal,
        "permanent": prmt
    })

print("\n=== All the Employee Details ===")

for i, emp in enumerate(employees):
    print(f"\n** Employee {i + 1} **")
    print("Employee id:", emp["id"])
    print("Employee name:", emp["name"])
    print("Employee age:", emp["age"])
    print("Employee department:", emp["dept"])
    print("Employee salary:", emp["salary"])
    print("Employee permanent:", emp["permanent"])