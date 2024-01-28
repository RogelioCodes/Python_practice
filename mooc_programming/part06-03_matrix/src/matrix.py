# write your solution here
def parse_file():
  lines = []
  with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            lines.append(parts)
  return lines

def matrix_sum():
    sum = 0
    
    lines = parse_file()
    for line in lines:
        for number in line:
            sum += int(number)
  
    return sum

def matrix_max():
    lines = parse_file()
    
    largest = int(lines[0][0])
    for line in lines:
        for number in line:
            if int(number) > largest:
                largest = int(number)
    return int(largest)

def row_sums():
    list_of_sums = []
    sum = 0
    lines = parse_file()
    for line in lines:
        sum = 0
        for number in line:
            sum += int(number)
        list_of_sums.append(sum)
    return list_of_sums


if __name__ == "__main__":
    
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())