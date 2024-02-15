class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}': '{', ']':'['}
        stack = []
       
        for c in s:
            if c not in hashmap:
                stack.append(c)
                continue
            print(f"c: {c}")
            #If a character is a closing parenthesis:
            if not stack or stack[-1] != hashmap[c]: #If the value in hashmap doesnt match parentheses OR stack is empty when we encounter a closing parenthesis
                return False
            stack.pop() #We pop whenever the closing bracket had a valid opening
        return not stack
        