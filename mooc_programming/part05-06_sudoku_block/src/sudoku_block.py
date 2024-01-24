# Write your solution here
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
  
       
   
   



