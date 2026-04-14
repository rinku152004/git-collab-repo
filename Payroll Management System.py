"""Create a payroll management system using OOP.
Requirements:
Create a base class Employee with attributes:
 name, emp_id, base_salary
Create subclasses:
FullTimeEmployee
ContractEmployee
Salary rules:
Full-time employee → base_salary + bonus (10%)
Contract employee → base_salary * hours_worked
Create a class PayrollSystem that:
Stores multiple employees
Calculates monthly salary for each
Displays salary slip in clean format

Payroll Management System
# =================================================================================================================
"""
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return 0  # overridden in child classes

    def display_salary_slip(self):
        salary = self.calculate_salary()

        
        print("            SALARY SLIP")
        
        print("Employee ID   :", self.emp_id)
        print("Employee Name :", self.name)
        print("Base Salary   :", self.base_salary)
        print("---------------------------------------")
        print("Total Salary  :", salary)
       

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary):
        super().__init__(name, emp_id, base_salary)

    def calculate_salary(self):
        bonus = self.base_salary * 0.10  # 10% bonus
        return self.base_salary + bonus

    def display_salary_slip(self):
        bonus = self.base_salary * 0.10
        total_salary = self.calculate_salary()

        
        print("         FULL-TIME SALARY SLIP")
        
        print("Employee ID   :", self.emp_id)
        print("Employee Name :", self.name)
        print("Base Salary   :", self.base_salary)
        print("Bonus (10%)   :", round(bonus, 2))
        print("---------------------------------------")
        print("Total Salary  :", round(total_salary, 2))
        print()


class ContractEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, hours_worked):
        super().__init__(name, emp_id, base_salary)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.base_salary * self.hours_worked  # hourly rate * hours

    def display_salary_slip(self):
        total_salary = self.calculate_salary()

        
        print("         CONTRACT SALARY SLIP")
        
        print("Employee ID     :", self.emp_id)
        print("Employee Name   :", self.name)
        print("Hourly Rate     :", self.base_salary)
        print("Hours Worked    :", self.hours_worked)
        print("---------------------------------------")
        print("Total Salary    :", round(total_salary, 2))



class PayrollSystem:
    def __init__(self):
        self.employees = []  # stores multiple employee objects

    def add_full_time_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")

        try:
            base_salary = float(input("Enter Base Salary: "))
            if base_salary < 0:
                print(" Salary cannot be negative!")
                return
        except:
            print(" Invalid Salary input!")
            return

        emp = FullTimeEmployee(name, emp_id, base_salary)
        self.employees.append(emp)
        print(" Full-Time Employee Added Successfully!")

    def add_contract_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")

        try:
            hourly_rate = float(input("Enter Hourly Rate: "))
            if hourly_rate < 0:
                print(" Hourly rate cannot be negative!")
                return
        except:
            print(" Invalid Hourly Rate input!")
            return

        try:
            hours_worked = int(input("Enter Hours Worked: "))
            if hours_worked < 0:
                print(" Hours cannot be negative!")
                return
        except:
            print(" Invalid Hours input!")
            return

        emp = ContractEmployee(name, emp_id, hourly_rate, hours_worked)
        self.employees.append(emp)
        print("Contract Employee Added Successfully!")

    def display_all_salary_slips(self):
        if len(self.employees) == 0:
            print(" No employees found!")
            return

        print("\n ===== ALL EMPLOYEE SALARY SLIPS =====")
        print()
        for emp in self.employees:
            emp.display_salary_slip()

    def calculate_payroll(self):
        if len(self.employees) == 0:
            print(" No employees found!")
            return

        print("\n========= MONTHLY PAYROLL SUMMARY =========")
        print("Emp ID\t\tName\t\tSalary")
        print("------------------------------------------------")

        for emp in self.employees:
            salary = emp.calculate_salary()
            print(emp.emp_id, "\t\t", emp.name, "\t\t", round(salary, 2))

        print("------------------------------------------------")


# -------------------------------
# Main Menu Driven Program
# -------------------------------
payroll = PayrollSystem()

while True:
    print("\n=========== PAYROLL MANAGEMENT MENU ===========")
    print("1. Add Full-Time Employee")
    print("2. Add Contract Employee")
    print("3. Show All Salary Slips")
    print("4. Payroll Summary (Monthly)")
    print("5. Exit")
    print("==============================================")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        payroll.add_full_time_employee()
    elif choice == "2":
        payroll.add_contract_employee()
    elif choice == "3":
        payroll.display_all_salary_slips()
    elif choice == "4":
        payroll.calculate_payroll()
    elif choice == "5":
        print("Exiting Payroll System... Thank you!")
        break
    else:
        print(" Invalid choice! Please enter 1 to 5.")



