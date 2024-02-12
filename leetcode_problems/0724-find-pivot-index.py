"""
#Logic:
We will first take the sum of all the numbers in the list. Then we will check, at every index, if our sumLeft and sumRight values are equal.

So we know that the total = sumleft + sumright and that the pivot index is where sumright == sumleft
So then we know that sumRight = total - sumLeft, but we must also subtract nums[i](the pivot value we are currently at)
So then we can simply check if both sumLeft and sumRight are equal, if not we will continue to iterate through the loop, 
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = 0
        for num in nums:
            total += num

        sumLeft = 0
        for i in range(len(nums)):
            sumRight = total - sumLeft - nums[i]

            if sumLeft == sumRight:
                return i
            sumLeft += nums[i] 
        
        return -1