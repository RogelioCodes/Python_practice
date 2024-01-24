# Write your solution here
# Write your solution here
def print_sudoku(sudoku: list):
    i = 1
    j = 1
    for row in sudoku:
       
        
        for item in row:
                if i <= 2:
                    if item == 0:
                            print("_", end = " ")
                    else:
                        print(item, end = " ")
                else:
                    
                    if item == 0:
                            print("_", end = "  ")
                    else:
                        print(item, end = "  ") 
                 
                    i = 0     
                i += 1
        if j <= 2:
            print("") 
        else:
            print("\n")
            j = 0
        
        j += 1

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_list = []
    for row in sudoku:
         temp = []
         for item in row:
              temp.append(item)
         new_list.append(temp)
        
    new_list[row_no][column_no] = number
    return new_list
