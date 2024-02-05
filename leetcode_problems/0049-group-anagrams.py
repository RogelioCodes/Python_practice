class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Logic:
        #We want to go through each string in the list, letter by letter, and make a list
        #This list represents the number of occurences of each letter in a given string
        #We will use this list as a key for our hashmap, where each word or string with the same number of occurences of each letter will be saved to
        
        res = defaultdict(list) # We initialize a dictionary with the default values being lists

        for s in strs:
            count = [0] * 26 #A list of 26 0s, one for each letter of the alphabet
            for ch in s:
                count[ord(ch) - ord('a')] += 1 #counts the number of occurences of each letter
            res[tuple(count)].append(s) #we append every word with the same number of occurences of each letter to our res hashmap
        return res.values()