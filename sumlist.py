def sum(list,i=0):
  if i==len(list):
    return 0
  return list[i] + sum(list,i+1)
    
list=[1,2,3,4,5]
sum=sum(list)
print("Sum is:",sum)