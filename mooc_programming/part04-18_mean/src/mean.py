# Write your solution here
def mean(list):
    sum = 0
    for item in list:
        sum += item
    avg = sum / (len(list))
    return avg 
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)