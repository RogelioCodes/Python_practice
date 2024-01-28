# write your solution here

def largest():
    largest = 0
    with open("numbers.txt") as new_file:
  
        for line in new_file:
            number = int(line)
            if number > largest:
                largest = number
            #print(line)
    return largest


#largest()