class Counting:
    def sorting(self,nums):
        # n=len(nums)
        mx=max(nums)

        freq=[0]*(mx+1)

        for i in nums:
            freq[i]+=1

        nums=[]
        for i in range(0,mx+1):
            while freq[i]>0:
                nums.append(i)
                freq[i]-=1

        return nums
    

counting=Counting()
nums=[0,2,1,0,5,4,3,1,2,6,3,5,4]
print(f"Sorted array is:{counting.sorting(nums)}")
