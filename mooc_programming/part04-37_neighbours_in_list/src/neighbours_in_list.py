
def longest_series_of_neighbours(list):
    longest = 1
    result = 1 
    for i in range(1, len(list)):
        if abs(list[i-1] - list[i]) == 1:
            result += 1
        else:
            result = 1
        
        longest = max(result, longest)
    return longest

