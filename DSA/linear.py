def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

# Corrected input section
mylist = []
size = int(input("Enter size of array: "))

for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    mylist.append(element)

print("Your list:", mylist)

x = int(input("Enter a number to search for: "))
result = linearSearch(mylist, x)

if result != -1:
    print("Found at index", result)
else:
    print("Not found")

