# Write your solution here
def sudoku_grid_correct(sudoku: list):
    for row in range(0, 9):
        if row_correct(sudoku, row) == False:
            return False
        
    for col in range(0,9):
        if column_correct(sudoku, col) == False:
            return False
    
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if block_correct(sudoku, row, col) == False:
                return False
    
    return True

    
def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_list = []
    for item in row: #Go through each item in a row
        if item in tokens: #if item is acceptable value
            if item not in new_list: #if item is acceptable value AND not a duplicate
                new_list.append(item) 
            else:
                return False

    return True

def column_correct(sudoku: list, column_no: int):
    tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_list = []
    for row in sudoku:
        #print(row[column_no])
        if row[column_no] in tokens:
            if row[column_no] not in new_list:
                new_list.append(row[column_no])
            else:
                return False
    #print(new_list)
    return True 

def block_correct(sudoku: list, row_no: int, column_no: int):
    tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_list = []
    for row in range(row_no, row_no+3):
        for element in range(column_no, column_no+3):
            number = sudoku[row][element]
            if number in tokens:
                if number not in new_list:
                    new_list.append(number)
                else:
                    return False
    return True
  
