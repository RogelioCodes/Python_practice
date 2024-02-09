"""
Logic:
    We start with two pointers, left and right, and we start at the second element in the list. This is because the array is already sorted, so the first element always stays the same.
    As we go through our loop, we will use the left variable to keep track of unique elements. 
    We know we have encountered a unique element when the elemement directly to the left of the right element and the right element do not have the same value (nums[r] != nums[r-1])
    Whenever we encounter a unique element, we will replace the element at the left counter with the element at the right counter, then increment our left pointer.

    Example [1,1,2] -> r = 2, l = 1, since these elements dont match we will swap nums[l] with nums[r] 
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = 1
       
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
          
        return l
   