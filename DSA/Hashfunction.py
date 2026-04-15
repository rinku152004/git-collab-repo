class Hash:
    def __init__(self):
        # Initialize my_list as an instance variable
        # self.my_list = [None] * 10 
        self.my_list = [[] for _ in range(10)]

    def hash_function(self, value):
        sum_of_chars = 0
        for char in value:
            sum_of_chars += ord(char)
        return sum_of_chars % 10

    def add(self, name):
    
        index = self.hash_function(name)
        self.my_list[index].append(name) # Multiple names can now coexist here
        print(f"Added '{name}' at index: {index}")

    def contains(self, name):
        
        index = self.hash_function(name)
    # Search the specific list at this index
        is_present = name in self.my_list[index]
        if is_present:
            print(f"'{name}' found at index {index} (Bucket contents: {self.my_list[index]})")
        else:
            print(f"'{name}' not found.")
        return is_present

# # Create an instance of the class
hash_table = Hash() 
while True:
    print("==== AVAILABLE OPTIONS ====")    
    print("1.Add")
    print("2.Check Availability")
    print("3.Exit")
    print("===========================")

    choice=(input("Enter your choice(1 to 3 only):"))

    if choice=="1":
        name=input("Enter name to add: ")
        hash_table.add(name)
        print("\nCurrent list state:", hash_table.my_list)
    elif choice=="2":
        name=input(f"Enter name to check: ")
        print(f"{name} is in the Hash Table: {hash_table.contains(name)}") 
    elif choice=="3":
        print("Exitingggg")
        break
    else:
        print("Pls Enter valid input....")
