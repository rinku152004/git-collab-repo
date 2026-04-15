class Bubble:
    def Bubble(nums):
        n=len(nums)

        for i in range(n):
            isSwap=0
            for j in range(n-i-1):
                if nums[j]> nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
                    isSwap+=1
            print(isSwap)
            # if not isSwap:
            #     break
            #     print("Array is already sorted.....")
        return nums
    nums=[3,4,7,9,80,34,23,10,12]
    print(f"Sorted Array is:{Bubble(nums)}")
