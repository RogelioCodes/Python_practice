"""
Logic:
Two pointer approach:
    We set a pointer to keep track of the character at the beginning of the string(left), and the end of the string(right).
    We will increment and decrement these pointers as we go through each character.
    If at any point, the left pointer meets the right pointer, we exit the loop.

    We must also have a check for whether or not a character is a valid character, we will skip over anything that is not an alpha numeric character.
    When we encounter a character that is not a letter or digit, we will increment or decrement the respective pointers
    
    If at any point we encounter a set of characters that do not match, we can return False as we know it is not a palindrome

    If we make it through the entire loop, we can return True as we know it must be a palindrome


"""
class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True
        
    def isAlphaNum(self, c: str):
            return(
                ord('A') <= ord(c) <= ord('Z')
                or ord('a') <= ord(c) <= ord('z')
                or ord('0') <= ord(c) <= ord('9')
            )