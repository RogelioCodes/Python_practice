class Solution:
    """
    We know that two numbers in the list will add up to a target value, so doing some algebra we also know that Target - nums[i] = diff because Target = nums[i] + nums[i]
    So we can save the index of each number, and take the difference of Target - nums[i] at each index.
    We then check if that difference was already in the hashmap, if it is, we know that we found our other number. This is because Target = nums[i] + diff
    For example:
    Target = 9. List = [2, 7, 11, 15]
    We know that Target = 9 - 2 and target = 9 - 7
    so we just have to find if 7 exists or if 2 exists in the hashmap:
    {2, 7, 9, 11}
    So once we reach index 7 at index 1, 2 will already be in the hashmap. So we will return the index of 2 and the index of 7
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, value in enumerate(nums):
            diff = target - value

            if diff in hashmap:
                return [ hashmap[diff], i ]

            hashmap[nums[i]] = i 
        