class Search:
    def Linear(self,nums,target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            
        return -1
    
linear=Search()
nums=[2,4,7,9,1,3,6,8]
target=int(input("Enter Number to search:"))
# nums=int(input("Enter list numbers:"))
print(f"Target number found at index {linear.Linear(nums,target)}")