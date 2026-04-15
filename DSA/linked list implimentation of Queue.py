# linked list implimentation of Queue
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.len=0

    def push(self,x):
        newNode= Node(x)
        self.len+=1
        if self.front is None:
            self.front= newNode
            self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode
        print(f"Element is pushed:{self.rear.data}")

    def pop(self):
        if self.front is None:
            print("Queue is Emptyyy")
            return
        x=self.front.data
        self.front=self.front.next
        self.len-=1
        if self.front is None:
           self.rear=None
        print(f"poped element is:{x}") 
    
    def getFront(self):
        if self.front is None:
            return -1
        print(f"Front of queue is:{self.front.data}") 
     
    def size(self):
        print(f"size of queue is:{self.len}") 
    
queue= Queue()

while True:
    print("-----List of queue Operations-----")
    print("1.push")
    print("2.pop")
    print("3.getFront")
    print("4.size")
    print("5.Exit")

    choice=input("Enter your choice (1-5) :")

    if choice=="1" or choice=="push" :
        x=int(input("Enetr number to push:"))
        queue.push(x)
    elif choice=="2" or choice=="pop" :
        queue.pop()
    elif choice=="3" or choice=="getFront" :
        queue.getFront()
    elif choice=="4" or choice=="size" :
        queue.size()
    elif choice=="5" or choice=="Exit" :
        print("Exitingggg....")
        break
    else:
        print("Enter valid number (1-5) only....Try Again..!")






        