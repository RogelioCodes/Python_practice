class Solution:
    #Logic:
    #We want to make a hashmap for each string, and count the number of occurences of each character in the string
    #We can then compare the values of these two hashmaps, if the number of occurences for any given character doesn't match, we return False
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #Default case
            return False

        hashmap_s, hashmap_t = {}, {}
        
        for i in range(len(s)):
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i], 0) #Here we increment the number of occurences of each character, initializing the value to 0 if it does not exist in the hashmap
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i], 0) # .get will grab the value of a letter in the hashmap, returning 0 if it does not exist in the hashmap
        
        for ch in hashmap_s:
            if hashmap_s[ch] != hashmap_t.get(ch, 0): #if the values do not match, we return False
                return False
        #We can return True once we have checked every key, value pair in both hashmaps
        return True