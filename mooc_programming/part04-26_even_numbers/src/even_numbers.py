# Write your solution here
def even_numbers(list):
    even_nums = []
    for item in list:
        if item % 2 == 0:
            even_nums.append(item)
    return even_nums