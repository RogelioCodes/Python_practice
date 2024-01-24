# Write your solution here
def all_the_longest(list):
    longest = list[0]
    new_list = []
    for item in list:
        #print(item)
        if len(item) > len(longest):
            longest = item

    new_list.append(longest)
    for item in list:
        if len(item) == len(longest) and item not in new_list:
            new_list.append(item)


    return new_list

