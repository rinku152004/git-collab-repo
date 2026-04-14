import math

def calculator(a,b,choice):
  match choice:
    case 1:
      return a+b
    case 2:
      return a-b
    case 3:
      return a*b
    case 4:
      return a/b
    case 5:
      return (a*b)/100
    case 6:
      return math.sqrt(a)
    case _:
      print("Invalid choice")
      
a= float(input("Enter first number:"))
b= float(input("Enter second number:"))

print("Choose an operation:")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Percentage")
print("6.Squareroot")

choice=int(input("Enter your choice(1-6):"))

result=calculator(a,b,choice)
print("result:",result)