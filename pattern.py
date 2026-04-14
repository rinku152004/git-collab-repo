n=4
k=0
for i in range(1,n+1):
  k=k+i
  
for i in range(n,0,-1):
  
  for j in range(i):
    print(k,end=" ")
    k-=1
  print(" ")
#ORR
print()
  
n=10
for i in range(4,0,-1):
  for j in range(i):
    print(n,end=" ")
    n-=1
  print(" ")
# o/p:
# 10 9 8 7
# 6 5 4
# 3 2
# 1


n=4
k=0
for i in range(1,n+1):
  k=k+i
  
for i in range(1,n+1):
  
  for j in range(i):
    print(k,end=" ")
    k+=1
  print(" ")
  k=k-(2*i)-1
  
# o/p:
# 10
# 8  9
# 5  6 7
# 1  2 3 4

print()  

n=5

for i in range(1,n):
   for j in range(i):
      print("*", end=" ")
   print("\n")

# output:
# *
# * *
# * * *
# * * * *
   
print("\n")
for i in range(n-1,0,-1):
   for j in range(i):
      print("*", end=" ")
   print("\n")

# output:
# * * * *
# * * *
# * *
# *


n=1
for i in range(1,5):
  for j in range(i):
    print(n,end=" ")
    n+=1
  print(" ")

# output:
# 1  
# 2 3  
# 4 5 6  
# 7 8 9 10  
 
n=10
for i in range(4,0,-1):
  for j in range(i):
    print(n,end=" ")
    n-=1
  print(" ")  


n=4
k=0
for i in range(1,n+1):
  k=k+i
  
for i in range(n,0,-1):
  s=k-i+1
  for j in range(i):
    print(s,end=" ")
    s+=1
  print(" ")
  k=k-i
 
# output:
# 7 8 9 10  
# 4 5 6
# 2 3
# 1

#1) Reverse string

def reverse(str):
  if len(str)==0:
    return str
  if len(str)==1:
    return str[0]
  return str[len(str)-1] + reverse(str[:len(str)-1])
    
x=reverse("rinku")
print(x)

# o/p: uknir

# 2) sum of list elements

def sum(list,i=0):
  if len(list)==i:
    return 0
  return list[i] + sum(list,i+1)
    
list=[1,2,3,4,5]
sum=sum(list)
print("Sum is:",sum)

# optional ) factorial of number

def fact(n):
  if n==0 or n==1:
    return 1
    
  else:
    return n*fact(n-1)
    
x=fact(4)
print(x)

# 3) count occurence of number

#List → [1, 4, 2, 4, 4, 9], Target → 4
def numcount(list,target,i=0):
  if len(list)==i:
    return 0
  if list[i]==target:
    return 1 + numcount(list,target,i+1)
  else:
    return numcount(list,target,i+1)
  
list=[1, 4, 2, 4, 4, 9]
n=4
print(numcount(list,n))

# o/p: 3

# 4)find max number from list

def maximum(list,i=0):
  if len(list)==i:
    return 0
  max=maximum(list,i+1)
  if list[i]>max:
    return list[i] 
  return max
    
list=[1,2,33,4,5]
x=maximum(list)
print("Maximum is:",x)

# o/p: 33

# 6) fibonacci series

def fib(n):
  if n==0:
    return 0
  if n==1:
    return 1
  return fib(n-1) + fib(n-2)
  
print(fib(5))

# o/p:13

# 8) count digits of any number 

def countdigit(n):
  if n==0:
    return 0
    
  return 1 + countdigit(n//10)
  
print(countdigit(n=11234))

# o/p: 5

# 10) power of any number


def power(a,n):
   if n==0:
     return 1
   else:
     return a * power(a,n-1)
     
print(power(2,3))

# o/p:8 

# 7)flatten the nested list

def flatten(lst):
  result=[]
  for item in lst:
      if isinstance(item,list):
         result.extend(flatten(item))
      else:
         result.append(item)
  return result
print(flatten([1, [2, 3], [4, [5]]]))

# o/p: [1,2,3,4,5]

# 5) check the pallindrome string

def pallindrome(str):
  str=str.replace(" ","").lower()
  
  if len(str)<=1:
    return True
    
  if str[0]!=str[-1]:
    return False
  
  return pallindrome(str[1:-1])
  
print(pallindrome("Race Car"))

print()
