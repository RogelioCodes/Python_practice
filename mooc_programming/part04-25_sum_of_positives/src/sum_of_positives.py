# Write your solution here
def sum_of_positives(list):
    sum = 0 
    for item in list:
        if item > 0:
            sum += item
    return sum

