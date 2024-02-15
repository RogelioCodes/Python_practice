"""
Logic:
We know that our return value must be a list so we will create a list to store our result (res)
We want to find all combinations. If we sort the array, we can make it so we do not have to run the calculations twice. 

sort input, 
for each first element, 
    find next two where -a = b+c, 
    if a=prevA, skip a, 
    if b=prevB skip b to elim duplicates; 
    
    to find b,c use two pointers, left/right on remaining list;

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            print(f"i: {i}, a: {a}")
            if i > 0 and a == nums[i - 1]: #This means it is the same value as before
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                print(f"{threeSum} = {a} + {nums[l]} + {nums[r]}")
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([ a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r :
                        l += 1 
        return res
                   