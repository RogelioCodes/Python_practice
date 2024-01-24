# Write your solution here
def everything_reversed(list):
    #how to reverse:
    #start at end
    #traverse packwards
    reversed_list = []
    i = len(list) - 1

    while i >= 0:
        reversed_word = ""
        x = len(list[i]) - 1

        while x >= 0:
            reversed_word += list[i][x]
            x -= 1
        #for letter in list[i]:
        #    reversed_word += letter

        reversed_list.append(reversed_word)
        i -= 1
    return reversed_list

