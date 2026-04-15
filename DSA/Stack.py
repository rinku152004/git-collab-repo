# List Implementation of Stack

class Stack:
    def __init__(self):
        self.st=[]

    def push(self,x):
        self.st.append(x)
        print("Number is added to stack ")
        print(f"Elements in stack are:{self.st}") 
        

    def pop(self):
        
        if len(self.st)==0:
            print("Stack is Empty... ")
            return
        x=self.st[-1]
        self.st.pop()
        print("Number is poped from stack")
        print(f"Popped element is :{x}")
        print(f"Elements left in stack are: {self.st}")

    def top(self):
        if len(self.st)==0:
            print("Stack is Empty... ")
            return
        print(f"Top element of stack is:{self.st[-1]}")
    
    def size(self):
        print(f"Size of stack is:{len(self.st)}")

stack= Stack()

while True:
    print("-----List of Stack Operations-----")
    print("1.push")
    print("2.pop")
    print("3.top")
    print("4.size")
    print("5.Exit")

    choice=input("Enter your choice (1-5) :")

    if choice=="1" or choice=="push" :
        x=int(input("Enetr number to push:"))
        stack.push(x)
    elif choice=="2" or choice=="pop" :
        stack.pop()
    elif choice=="3" or choice=="top" :
        stack.top()
    elif choice=="4" or choice=="size" :
        stack.size()
    elif choice=="5" or choice=="Exit" :
        print("Exitingggg....")
        break
    else:
        print("Enter valid number (1-5) only....Try Again..!")


