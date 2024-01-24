# Write your solution here
def shortest(list):
    shortest = list[0]

    for item in list:
        #print(item)
        if len(item) < len(shortest):
            shortest = item
    #print(shortest)
    return shortest

