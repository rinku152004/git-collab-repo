n=15
for i in range(n):
    k=7-i
    for j in range(n):
        # k=7-j
        p=j-7

        #border
        if (i==0 or i==14) and 0<j<14:
            print("0",end=" ")
        elif ((j==0 or j==14) and 0<=i<=14)or(i==7 and j==7):
            print("o",end=" ")
        
        # elif (i==7 and j==7):
        #     print("m",end=" ")  

        #first triangle
        elif (0<i<7 and 0<j<7) and i<=j:
            print(k,end=" ")
            k-=1

        #second triangle
        elif (0<i<7 and 7<j<14) and (n-2-i)<j:
            print(i,end=" ")
            i-=1
        
        #third triangle
        elif (7<i<14 and 0<j<7) and (i+j)<=14:
            print(j,end=" ")

        #fourth triangle
        elif (7<i<14 and 7<j<14) and i>=j:
            print(p,end=" ")
            
        else:
            print(" ",end=" ")

        
    print()