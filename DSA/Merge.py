class Merge:
    @staticmethod
    def merge(nums,l,mid,r):
        a=[] #store l to mid elements
        b=[] #store mid+1 to r elements
        for i in range(l,mid+1):
            a.append(nums[i])
        for i in range(mid+1,r+1):
            b.append(nums[i])

        i,j,k=0,0,l
        while k<=r:
            if j==len(b):
                nums[k]=a[i]
                i+=1
                k+=1
            elif i==len(a):
                nums[k]=b[j]
                j+=1
                k+=1

            elif a[i]<b[j]:
                nums[k]=a[i]
                i+=1
                k+=1
            else:
                nums[k]=b[j]
                j+=1
                k+=1



    def MergeSort(self,nums,l,r):
        # base case
        if l>=r:
            return
        # recursive case
        mid=(l+r)//2
        # l to mid
        self.MergeSort(nums,l,mid)
        self.MergeSort(nums,mid+1,r)
        self.merge(nums,l,mid,r)

    def SortArray(self,nums):
        self.MergeSort(nums,0,len(nums)-1)
        return nums

# sort=Merge()
nums=[2,5,1,3,4,9,12,6,20]
# nums = [2, 5, 1, 3, 4,56,22,34,11,57,90,45]
sort=Merge()
print(f"Sorted array is:{sort.SortArray(nums)}")
        
# print()
# In other Approach or diff logic conditions
# class Merge:
#     @staticmethod
#     def merge(nums, l, mid, r):
#         # store l to mid elements
#         a = nums[l : mid + 1]
#         # store mid+1 to r elements
#         b = nums[mid + 1 : r + 1]
#         i, j, k = 0, 0, l

#         while i < len(a) and j < len(b):
#             if a[i] < b[j]:
#                 nums[k] = a[i]
#                 i += 1
#             else:
#                 nums[k] = b[j]
#                 j += 1
#             k += 1
        
#         # Copy remaining elements of a, if any
#         while i < len(a):
#             nums[k] = a[i]
#             i += 1
#             k += 1
        
#         # Copy remaining elements of b, if any
#         while j < len(b):
#             nums[k] = b[j]
#             j += 1
#             k += 1

#     def MergeSort(self, nums, l, r):
#         # base case
#         if l >= r:
#             return
#         # recursive case
#         mid = (l + r) // 2
#         # l to mid
#         self.MergeSort(nums, l, mid)
#         self.MergeSort(nums, mid + 1, r)
#         self.merge(nums, l, mid, r)

#     def SortArray(self, nums):
#         self.MergeSort(nums, 0, len(nums) - 1)
#         return nums

# nums = [2, 5, 1, 3, 4,56,22,34,11,57,90,45]
# # Create an instance of the class to call the method
# sorter = Merge() 
# print(f"Sorted array is:{sorter.SortArray(nums)}")
