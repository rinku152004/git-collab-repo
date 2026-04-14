# n=6
# for i in range(n,0,-1):
#     for j in range(0,n-i):
#         print(" ",end=" ")

#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

# print()
# n=6
# for i in range(0,n+1):
#     k=i
#     for j in range(n+1,0,-1):
        
#         if k<j:
#             print(" ",end=" ")
#         else:
#             print(k,end=" ")
#             k-=1
#     print()

# n=6
# for i in range(6):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# print()
# n=6
# for i in range(n,0,-1):

#     for j in range(0,i):
#         print(j+1,end=" ")
          
#     print()
# print()


# complex pattern homework

w=14
print("o"+" 0"*(w-1)+" o")
n=6
for i in range(n,0,-1):
    print("o",end=" ")
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i+1,0,-1):
        print(k,end=" ")
    print("o")
print("o"+" "*13+"o"+" "*13+"o")
for i in range(n,0,-1):
    print("o",end=" ")
    for k in range(i):
        print(k+1,end=" ")
    for j in range(n-i+1):
        print(" ",end=" ")
    for k in range(n-i+1):
        print(k+1,end=" ")
    for j in range(i-1):
        print(" ",end=" ")
    print("o")   

print("o"+" 0"*(w-1)+" o")   


print()

# new pattern with center R
n=4
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i+1,0,-1):
        print(k,end=" ")
    print()
    
print("        R    ")
# if i==5 and j==5:
# print("R",end=" ")
for i in range(n,0,-1):
    for k in range(i):
        print(k+1,end=" ")
    for j in range(n-i+1):
        print(" ",end=" ")
    for k in range(n-i+1):
        print(k+1,end=" ")
    for j in range(i-1):
        print(" ",end=" ")
    print()
    
