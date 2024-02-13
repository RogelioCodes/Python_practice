"""
Logic:
Set two pointers and iterate through the entire list.
Use a while loop to count the number appearances each time we encounter a new element. 

Once we have the count, we can take the minimum of that value and two(because we only want two occurences), and use that to swap our right and left elements two times, making sure to increment our left pointer

"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, r = 0, 0

        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r+1]:
                r += 1
                count += 1
            
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1 #Iterates r to get to the beginning of the next streak, on the next iteration
        return l