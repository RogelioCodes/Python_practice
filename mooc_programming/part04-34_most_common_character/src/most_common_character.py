# Write your solution here
def most_common_character(str):
    #go throuhg each letter in string
    #count
    most_common = str[0]
    for character in str:
        if str.count(character) > str.count(most_common):
            most_common = character
    return most_common