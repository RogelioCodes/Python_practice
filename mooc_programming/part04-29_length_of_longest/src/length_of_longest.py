# Write your solution here
def length_of_longest(list):
    longest = list[0]

    for item in list:
        #print(item)
        if len(item) > len(longest):
            longest = item
   
    return len(longest)


"""
my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)
"""
