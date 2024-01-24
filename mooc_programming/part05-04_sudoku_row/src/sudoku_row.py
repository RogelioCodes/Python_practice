# Write your solution here
def row_correct(sudoku: list, row_no: int):
    count = 0
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

