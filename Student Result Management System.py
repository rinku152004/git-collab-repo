"""Student Result Manageselfnt System
# -------------------------------"""

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  # list of 5 subject marks

    def calc_total(self):
        total = 0
        for m in self.marks:
            total = total + m
        return total

    def calc_percentage(self):
        total = self.calc_total()
        percentage = total / 5
        return percentage

    def calc_grade(self):
        percentage = self.calc_percentage()

        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "Fail"

    def display_result(self):
        total = self.calc_total()
        percentage = self.calc_percentage()
        grade = self.calc_grade()

        print("\n------------------------------------")
        print("           STUDENT RESULT")
        print("--------------------------------------")
        print("Roll No     :", self.roll_no)
        print("name        :", self.name)

        print("Marks       :", end=" ")
        for i in range(5):
            print(self.marks[i], end=" ")
        print()

        print("Total Marks :", total, "/ 500")
        print("Percentage  :", round(percentage, 2), "%")
        print("Grade       :", grade)
        print("--------------------------------------")


class ResultSystem:
    def __init__(self):
        self.students = []  # list of Student objects

    def add_student(self):
        try:
            roll_no = int(input("Enter Roll No: "))
        except:
            print(" Invalid Roll No! Must be a number.")
            return

        # Check duplicate roll no
        for s in self.students:
            if s.roll_no == roll_no:
                print(" Roll No already exists! Try another.")
                return

        name = input("Enter name: ")

        marks = []
        print("Enter marks for 5 subjects (0-100):")
        for i in range(5):
            while True:
                try:
                    m = int(input(f"Subject {i+1}: "))
                    if m < 0 or m > 100:
                        print(" Marks must be between 0 to 100.")
                    else:
                        marks.append(m)
                        break
                except:
                    print(" Invalid input! Enter integer marks.")

        student = Student(roll_no, name, marks)
        self.students.append(student)
        print(" Student Added Successfully!")

    def remove_student(self):
        if len(self.students) == 0:
            print(" No students available to remove.")
            return

        try:
            roll_no = int(input("Enter Roll No to remove: "))
        except:
            print(" Invalid Roll No!")
            return

        for i in range(len(self.students)):
            if self.students[i].roll_no == roll_no:
                del self.students[i]
                print(" Student Removed Successfully!")
                return

        print(" Student not found!")

    def search_student(self):
        if len(self.students) == 0:
            print(" No students available.")
            return

        try:
            roll_no = int(input("Enter Roll No to search: "))
        except:
            print(" Invalid Roll No!")
            return

        for s in self.students:
            if s.roll_no == roll_no:
                s.display_result()
                return

        print(" Student not found!")

    def display_all_results(self):
        if len(self.students) == 0:
            print(" No student records found.")
            return

        print("\n================ ALL STUDENTS RESULTS ================")
        for s in self.students:
            s.display_result()

    def class_topper(self):
        if len(self.students) == 0:
            print(" No students available.")
            return

        topper = self.students[0]
        highest = topper.calc_percentage()

        for i in range(1, len(self.students)):
            per = self.students[i].calc_percentage()
            if per > highest:
                highest = per
                topper = self.students[i]

        print("\n ======= CLASS TOPPER =======")
        topper.display_result()

    # Optional Feature: Update Marks
    def update_marks(self):
        if len(self.students) == 0:
            print(" No students available.")
            return

        try:
            roll_no = int(input("Enter Roll No to update marks: "))
        except:
            print(" Invalid Roll No!")
            return

        for s in self.students:
            if s.roll_no == roll_no:
                new_marks = []
                print("Enter NEW marks for 5 subjects (0-100):")

                for i in range(5):
                    while True:
                        try:
                            m = int(input(f"Subject {i+1}: "))
                            if m < 0 or m > 100:
                                print(" Marks must be 0 to 100.")
                            else:
                                new_marks.append(m)
                                break
                        except:
                            print(" Invalid input! Enter integer marks.")

                s.marks = new_marks
                print(" Marks Updated Successfully!")
                return

        print(" Student not found!")

    #  Optional Feature: Pass/Fail Count
    def pass_fail_count(self):
        if len(self.students) == 0:
            print(" No students available.")
            return

        passed = 0
        failed = 0

        for s in self.students:
            grade = s.calc_grade()
            if grade == "Fail":
                failed += 1
            else:
                passed += 1

        print("\n PASS STUDENTS :", passed)
        print(" FAIL STUDENTS :", failed)

    #  Optional Feature: Rank Students (based on %)
    def rank_students(self):
        if len(self.students) == 0:
            print(" No students available.")
            return

        # simple bubble sort using loops 
        for i in range(len(self.students)):
            for j in range(i + 1, len(self.students)):
                if self.students[j].calc_percentage() > self.students[i].calc_percentage():
                    temp = self.students[i]
                    self.students[i] = self.students[j]
                    self.students[j] = temp

        print("\n========= STUDENT RANK LIST =========")
        print("Rank\tRoll No\t Name\t\tPercentage")
        print("--------------------------------------")

        for i in range(len(self.students)):
            print(i + 1, "\t", self.students[i].roll_no, "\t", self.students[i].name,
                  "\t\t", round(self.students[i].calc_percentage(), 2))


# -------------------------------
# Main Program (selfnu Driven)
# -------------------------------
rs = ResultSystem()

while True:
    print("\n=========== RESULT MANAGEMENT MENU ===========")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student Result")
    print("4. Display All Results")
    print("5. Class Topper")
    print("6. Update Marks ")
    print("7. Pass/Fail Count ")
    print("8. Rank List ")
    print("9. Exit")
    print("=============================================")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        rs.add_student()
    elif choice == "2":
        rs.remove_student()
    elif choice == "3":
        rs.search_student()
    elif choice == "4":
        rs.display_all_results()
    elif choice == "5":
        rs.class_topper()
    elif choice == "6":
        rs.update_marks()
    elif choice == "7":
        rs.pass_fail_count()
    elif choice == "8":
        rs.rank_students()
    elif choice == "9":
        print(" Exiting... Thank you!")
        break
    else:
        print(" Invalid choice! Please enter between 1 to 9.")
