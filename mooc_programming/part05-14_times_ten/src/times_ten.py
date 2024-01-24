# Write your solution here
def times_ten(start_index: int, end_index: int):
    my_dict = dict()
    for d in range(start_index, end_index+1):
        my_dict[d] = d * 10
    return my_dict
#d = times_ten(3, 6)
#print(d)