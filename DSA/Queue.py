# class Queue:
#     def __init__(self):
#         pass

#     def push(self):


# List Implementation of queue

class Queue:
    def __init__(self):
        self.que=[]
        self.front=-1
        # self.rear=-1

    def push(self,x):
        if self.front== -1:
            self.front=0
        self.que.append(x)
        print("Number is added to queue ")
        print(f"Elements in queue are:{self.que}") 
        

    def pop(self):
        
        if len(self.que)==0:
            print("queue is Empty... ")
            return
        x=self.que[self.front]
        self.front+=1
        if self.front== len(self.que):
            self.front=-1
            self.que=[]
        # self.que.pop()
        print("Number is poped from queue")
        print(f"Popped element is :{x}")
        print(f"Elements left in queue are: {self.que}")

    def getFront(self):
        if len(self.que)==0:
            print("queue is Empty... ")
            return
        print(f"Top element of queue is:{self.que[self.front]}")
    
    def size(self):
        if self.front==-1:
            return 0
        print(f"Size of queue is:{len(self.que) - self.front}")

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


