# Write your solution here

def palindromes(word):
    reverse = word[::-1]
    tokens1 = [*word]
    tokens2 = [*reverse]
    i = 0
   
    for letter in tokens1:
      
       if letter != tokens2[i]:
           return False
       i += 1
       # if tokens1[i]
    

    return True


# Note, that at this time the main program should not be written inside

while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word) == True:
            print(f"{word} is a palindrome!")
            break
        else:
            print(f"that wasn't a palindrome")
# block!
