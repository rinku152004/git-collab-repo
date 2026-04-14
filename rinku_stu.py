class Student:
    def __init__(self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks
    
    def calculate_total(self):
        total=0
        for m in self.marks:
            total=total+m
        return total

    def calculate_pr(self):
        total=self.calculate_total()
        percentage=total/5
        return percentage
    
    def calculate_grade(self):
        percentage = self.calculate_pr()

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

    def display_r(self):
        total = self.calculate_total()
        percentage = self.calculate_pr()
        grade = self.calculate_grade()

        print("\n--------------------------------------")
        print("           STUDENT RESULT")
        print("--------------------------------------")
        print("Roll No     :", self.roll_no)
        print("Name        :", self.name)

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
        self.student=[]
    
    def add_s(self):
        roll_no = int(input("Enter Roll No: "))
        name=input("Enter name :")

        marks=[]


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
        self.student.append(student)
        print(" Student Added Successfully!")


    def remove_s(self):
        if len(self.student) == 0:
            print(" No students available to remove.")
            return

        try:
            roll_no = int(input("Enter Roll No to remove: "))
        except:
            print(" Invalid Roll No!")
            return

        for i in range(len(self.student)):
            if self.student[i].roll_no == roll_no:
                del self.student[i]
                print(" Student Removed Successfully!")
                return

        print(" Student not found!")


    def search_s(self):
        if len(self.student) == 0:
            print(" No students available.")
            return

        try:
            roll_no = int(input("Enter Roll No to search: "))
        except:
            print(" Invalid Roll No!")
            return

        for s in self.student:
            if s.roll_no == roll_no:
                s.display_r()
                return

        print(" Student not found!")


    def display_all_r(self):
        if len(self.student) == 0:
            print(" No student records found.")
            return

        print("\n================ ALL STUDENT RESULTS ================")
        for s in self.student:
            s.display_r()

    def class_toper(self):
        if len(self.student) == 0:
            print(" No students available.")
            return

        topper = self.student[0]
        highest = topper.calculate_pr()

        for i in range(1, len(self.student)):
            per = self.student[i].calculate_pr()
            if per > highest:
                highest = per
                topper = self.student[i]

        print("\n ===== CLASS TOPPER =====")
        topper.display_r()

system = ResultSystem()

while True:
    print("\n=========== RESULT MANAGEMENT MENU ===========")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student Result")
    print("4. Display All Results")
    print("5. Class Topper")
    print("6. Exit")
    # print("6. Update Marks (Optional)")
    # print("7. Pass/Fail Count (Optional)")
    # print("8. Rank List (Optional)")
    # print("9. Exit")
    print("=============================================")

    choice = input("Enter your choice (1-5): ")

    match choice:
        case "1":
            system.add_s()
        case "2":
            system.remove_s()
        case "3":
            system.search_s()
        case "4":
            system.display_all_r()
        case "5":
            system.class_toper()
        case "6":
            print("Exittttt")   
            break 
        case _:
            print("plz enter valid choies  (1-5) : ")


    
        

        
