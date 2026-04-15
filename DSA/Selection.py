class Selections:
    def Selection(nums):
        n=len(nums)

        for i in range(n):
            min=nums[i]
            ind=i
            for j in range(i+1,n):
                if nums[j]<min:
                    min=nums[j]
                    ind=j

            temp=nums[i]
            nums[i]=nums[ind]
            nums[ind]=temp

        return nums
    print(f"Sorted array is:{Selection([8,3,4,1,6,8,92])}")
      