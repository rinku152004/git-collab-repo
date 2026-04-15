class Insertion:
    def Insertion(nums):
        n=len(nums)
    
        for i in range(1,n):
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        return nums
    print(f"Sorted array is:{Insertion([3,2,8,1,5,7])}")