class ArrayMerge:
    def Merge(self,nums1,m,nums2,n):
        i=m-1
        j=n-1
        k=m+n-1

        while j>=0:
            if i<0 or nums2[j]>nums1[i]:
                nums1[k]=nums2[j]
                k-=1
                j-=1
            else:
                nums1[k]=nums1[i]
                k-=1
                i-=1
            
        return nums1


arr=ArrayMerge()
nums1=[1,2,3,0,0,0]
nums2=[4,5,6]
m=3
n=3
print(f"Merged array is: {arr.Merge(nums1,m,nums2,n)}")
print()

class ArrayMerge:
    def Merge(self, nums1, m, nums2, n):
        # m = actual elements in nums1, n = actual elements in nums2
        i = m - 1      # End of actual numbers in nums1
        j = n - 1      # End of nums2
        k = m + n - 1  # End of the total space in nums1
        
        while j >= 0:
            # Check i >= 0 to avoid index errors if nums1 is exhausted first
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return nums1

# Corrected test case data
arr = ArrayMerge()
nums1 = [1, 2, 4, 0, 0, 0]  # First 3 elements MUST be sorted
nums2 = [3, 5, 6]           # MUST be sorted
m = 3  # Number of actual data elements in nums1
n = 3  # Number of elements in nums2

print(f"Merged array is: {arr.Merge(nums1, m, nums2, n)}")

print()
class ArrayMerge:
    def Merge(self, nums1, m, nums2, n):
        # 1. Sort the valid portions of both arrays first
        temp1 = sorted(nums1[:m])
        nums1[:m] = temp1
        nums2.sort()

        # 2. Your two-pointer logic (now it works!)
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return nums1

# Test Case
arr = ArrayMerge()
nums1 = [2, 4, 1, 0, 0, 0] # m=3 elements
nums2 = [6, 3, 5]          # n=3 elements
print(f"Merged array is: {arr.Merge(nums1, 3, nums2, 3)}")

