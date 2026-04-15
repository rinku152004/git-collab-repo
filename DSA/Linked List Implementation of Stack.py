#Linked List Implementation of Stack
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        # self.st=st
        self.top=None
        self.len=0

    def push(self,x):
        self.len+=1
        if self.top is None:
            self.top=Node(x)
            print("Number is added to stack ")
            
        else:
            newNode= Node(x)
            newNode.next=self.top
            self.top= newNode
            
            # self.display()
            # newNode=self.top
            print("Number is added to stack ")
            self.display()
            # print(f"Elements in stack are: {x}")
            

    def pop(self):
        if self.top==None:
            print("Stack is empty....")
            return
        
        x=self.top.data
        self.top=self.top.next
        self.len-=1
        print("Number is poped from stack")
        print(f"Popped element is :{x}")
        # self.display()
        return x
        # print(f"Elements left in stack are: {self}")

    def display(self):
        newNode=self.top
        if newNode is None:
            print("Elements in stack are:[]")
            return
        elements=[]
        while newNode:
            elements.append(newNode.data)
            newNode=newNode.next
        print(f"Elements in stack are: {elements}")
    
    def getTop(self):
        if self.top==None:
            print("Stack is empty....")
            return
        print(f"Top element of stack is:{self.top.data}") 
        
    def size(self):
        print(f"Size of stack is:{self.len}") 

stack=Stack()
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
        #print("Element is added to stack")
    elif choice=="2" or choice=="pop" :
        stack.pop()
    elif choice=="3" or choice=="top" :
        stack.getTop()
    elif choice=="4" or choice=="size" :
        stack.size()
    elif choice=="5" or choice=="Exit" :
        print("Exitingggg....")
        break
    else:
        print("Enter valid number (1-5) only....Try Again..!")




