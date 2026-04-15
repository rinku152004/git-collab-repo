class Quick:
    # @staticmethod
    def partition(self,nums,l,r):
        pivot=nums[r]
        start=l

        for i in range(l,r+1):
            if nums[i]<= pivot:
                temp=nums[i]
                nums[i]=nums[start]
                nums[start]=temp
                start+=1
        return start-1
        
    def quickSort(self,nums,l,r):
        # base case
        # if l>=r:
        #     return
        if l<r:
            p=self.partition(nums,l,r)

            self.quickSort(nums,l,p-1)
            self.quickSort(nums,p+1,r)

    def sortArray(self,nums):
        n=len(nums)
        self.quickSort(nums,0,n-1)

        return nums
nums=[5,2,8,6,1,4,9]  
sort=Quick()
# nums=[5,2,8,6,1,4,9]
print(f"Sorted array is:{sort.sortArray(nums)}")


print()
# sorting using diff logic

class Quick:
    def quick_sort_helper(self, nums, low, high):
        """Helper function for the recursive quick sort logic."""
        if low < high:
            # pi is the partitioning index, nums[pi] is now at the right place
            pi = self.partition(nums, low, high)
            self.quick_sort_helper(nums, low, pi)  # Recursively sort left sub-array
            self.quick_sort_helper(nums, pi + 1, high) # Recursively sort right sub-array
        return nums

    def partition(self, nums, low, high):
        """
        This function takes the first element as pivot, places the pivot 
        element at its correct position in a sorted array, and places all 
        smaller elements to the left of the pivot and all greater elements 
        to the right of the pivot using Hoare's partition scheme.
        """
        pivot = nums[low]
        i = low - 1
        j = high + 1
        while True:
            # Move the left index 'i' to the right until an element greater than or equal to the pivot is found
            i += 1
            while nums[i] < pivot:
                i += 1
            # Move the right index 'j' to the left until an element smaller than or equal to the pivot is found
            j -= 1
            while nums[j] > pivot:
                j -= 1
            # If pointers cross, partition is complete
            if i >= j:
                return j
            # Swap elements at i and j
            nums[i], nums[j] = nums[j], nums[i]

    def main(self, nums):
        """Main method to initiate the quick sort."""
        n = len(nums)
        if n == 0:
            return []
        self.quick_sort_helper(nums, 0, n - 1)
        return nums

# Example Usage:
nums = [5, 2, 1, 4, 3]
sort = Quick()
print(f"Sorted array is: {sort.main(nums)}") 
# Example with another list:
nums_alt = [5, 2, 8, 6, 1, 4, 9]
print(f"Sorted alternate array is: {sort.main(nums_alt)}")
