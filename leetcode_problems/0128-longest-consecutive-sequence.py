"""
Logic:
Add each number to a hashset. For each number, if num-1 doesn't exist, we count the consecutive nums after num.

For each number, we can find the start of a sequence by iterating through the list and subtracting 1 from the current element.
We know that if n-1 is not in the list of numbers, then we must be at the start of a sequence. 

Once we find the start of a sequence, we will begin a counter(length), and loop through a while loop that will break whenever we find the element that breaks the sequence.
The element that breaks the sequence is any element that is not inside of our set of numbers. For example:
given the list {100, 4, 200, 1, 3, 2}, we know that 5 would break our sequence, because it is not in our set.

We will then compare the length of that sequence with the current longest sequence.

Once we are done with our loop, we can return our longest number.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for num in nums: 
            if num-1 not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

