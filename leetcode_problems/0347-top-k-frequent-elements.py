class Solution:
    #Logic:
    #We will create a hashmap and a lists of lists
    #The hashmap will be used to count the number of occurences for each number
    #The list will contain a list for each index of the original list, so for [1,2,3] we would have [ [], [], [], []], with the extra being added to account for index 0
    #For this list, i represents the count, and we will save any number with the same amount of occurences into the same list

    #1. We will first count the number of occurences of each number in the list, and save those to our hashmap
    #2. We will go through each item in our hashmap, and save every number into the bucket list, where i denotes the number of occurences for a number: [1, 2, 2, 3, 4] -> [ [], [1,3,4], [2], [], [], [] ]
    #3. We will go through each bucket in our bucket list, and append each value to our result
    #4. Since our bucket list will have the elements that appear most at the end, we can start at the end and stop once the number of elements in res is equal to K
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = {}
       freq = [ [] for i in range(len(nums) + 1)] # add one to account for 0

       for num in nums:
           count[num] = 1 + count.get(num, 0)

       for n, c in count.items():
           freq[c].append(n)

       res = []
       for n in range(len(freq) - 1, 0, -1): # Since our bucket list will have the elements that appear most at the end, we can start at the end and stop once the number of elements in res is equal to K
           for num in freq[n]:
               res.append(num)

               if len(res) == k:
                   return res