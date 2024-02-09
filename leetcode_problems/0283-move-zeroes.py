"""
Logic:
We will start with two pointers, at the same index. 
Anytime we do not see a zero, we will swap our left and right elements, and increment our left pointer by one
We will increment our right pointer on every iteration of the loop

The left pointer tells us where to put the non zero element

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
    
   
        return nums