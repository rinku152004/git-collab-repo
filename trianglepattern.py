# n=int(input("enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()

# print()
n=int(input("enter the number of rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

print()
n=int(input("enter the number of rows:"))
for i in range(n):
    for j in range(n-1-i):
        print(" ",end=" ")
    for j in range((n-1-i),n+i):
        if (i+j)%2==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()