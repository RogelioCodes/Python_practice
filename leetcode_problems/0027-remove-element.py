"""
We will initialize two pointers, at index 0. 
Anytime the element on the right is not equal to the target value, we will swap the left and right elements, making sure to increment our left pointer
We will increment our right pointer on every iteration

The left pointer tells us where to put the current element(when it is not 0)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
    
   
        return l
