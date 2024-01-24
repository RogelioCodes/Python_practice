# Write your solution here
def distinct_numbers(list):
    new_list = []
    for item in list:
        if item not in new_list:
            new_list.append(item)
    new_list.sort()
    return new_list