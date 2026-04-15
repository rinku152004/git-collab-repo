# # Queue using two stacks
class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self,x):
        
        while len(self.s1)>0:
            self.s2.append(self.s1[len(self.s1)-1])
            self.s1.pop()
        self.s1.append(x)
        
        while len(self.s2)>0:
            self.s1.append(self.s2[len(self.s2)-1])
            self.s2.pop()
        print(f"{x} is added to queue ")

    def pop(self):
        if self.empty():
            print("Queue is empty. Cannot pop.")
            return None
        x=self.s1[len(self.s1)-1]
        self.s1.pop()
        print("Number is poped from queue")
        print(f"Popped element is :{x}")

    def peek(self):
        if self.empty():
            print("Queue is empty. Cannot peek.")
            return None
        # The front element is the last element in the current s1 list structure
        x = self.s1[0] 
        print(f"Front element is: {x}") 
    
    def empty(self):
        is_empty = len(self.s1) == 0
        print(f"Is queue empty? {is_empty}")
        return is_empty
    
queue=Queue()

while True:
    print("\n----- List of Queue Operations -----")
    print("1. Push (Enqueue)")
    print("2. Pop (Dequeue)")
    print("3. Peek (View front element)")
    print("4. Empty (Check if queue is empty)")
    print("5. Exit")
    print("--------------------------------------")

    choice=input("Enter your choice (1-5) :")

    if choice=="1" :
        x=int(input("Enetr number to push:"))
        queue.push(x)
    elif choice=="2" :
        queue.pop()
    elif choice=="3" :
        queue.peek()
    elif choice=="4" :
        queue.empty()
    elif choice=="5" :
        print("Exitingggg....")
        break
    else:
        print("Enter valid number (1-5) only....Try Again..!")

