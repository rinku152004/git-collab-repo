class ColorSort:
    def colors(self,nums):
        left=0
        right=len(nums)-1
        i=0
        while i<=right:
            if nums[i]==1:
                i+=1
            elif nums[i]==0:
                temp=nums[i]
                nums[i]=nums[left]
                nums[left]=temp
                i+=1
                left+=1
            elif nums[i]==2:
                temp=nums[i]
                nums[i]=nums[right]
                nums[right]=temp
                right-=1
        return nums
    
color=ColorSort()
nums=[0,1,2,2,0,1,2,0,1,0,2]
print(f"Sorted array of colors is: {color.colors(nums)}")
