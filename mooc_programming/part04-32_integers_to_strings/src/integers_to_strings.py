# Write your solution here
def formatted(numbers_list):
    formatted_list = [] #formatted to two decimal points

    for item in numbers_list:
        formatted_item = "{:.2f}".format(item)
        formatted_list.append(formatted_item)
    return formatted_list
