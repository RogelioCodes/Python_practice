class Solution:
    #Logic:
    #We will start by creating and initializing an array of 1s
    #We will then update each element in that array with the product of every number in the array that came before it
    #We will then go through the array backwards, keeping track of the postfix, with the postfix beginning at 1
    #As we go through the original array backwards, we will multiply it by the postfix, and then increment the postfix by multiplying it with the corresponding number at nums[i]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(1,len(nums)):
            res[i] *= res[i-1] * nums[i-1]
        
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            print(f"i: {i} nums[i]: {nums[i]}")
            res[i] *= postfix
            postfix *= nums[i]
        return res
 
        [1, 1, 2, 6]
        #[1,1,2, 6*1] postfix = 1 * 2
        [1,1,4,6]