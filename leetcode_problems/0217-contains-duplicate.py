class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #We will initialize a hashmap and add every number in the list to it
        #If the number is already in the hashmap, we have found a duplicate and can return False
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                return True
        return False
        