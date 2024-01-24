# Write your solution here
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
