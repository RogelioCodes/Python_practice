# Write your solution here
def no_vowels(str):
    vowels = "AaEeIiOoUu"
    for vowel in vowels:
        str = str.replace(vowel, '')
    return str

