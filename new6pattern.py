n=int(input("pls enter value of n: "))
for i in range((2*n)+3):
    for j in range((2*n)+3):
        k=(n+1)-j
        p=j-(n+1)
        x=(2*n)+2
        #border
        if (i==0 or i==x) and 0<j<x:
            print("0",end=" ")
        elif j==0 or j==x and 0<=i<=x or(i==(n+1) and j==(n+1)):
            print("0",end=" ")
        
        # elif (i==7 and j==7):
        #     print("m",end=" ")  

        #first triangle
        elif (0<i<n+1 and 0<j<n+1) and i<=j:
            print(k,end=" ")
            k-=1

        #second triangle
        elif ((0<i<(n+1) and (n+1)<j<x)) and (x-i-1)<j:
            print(i,end=" ")
            i-=1
        
        #third triangle
        elif ((n+1)<i<x and 0<j<(n+1)) and (i+j)<=x:
            print(j,end=" ")

        #fourth triangle
        elif ((n+1)<i<x and (n+1)<j<x) and i>=j:
            print(p,end=" ")
            
        else:
            print(" ",end=" ")

        
    print()
