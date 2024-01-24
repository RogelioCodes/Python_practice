# Write your solution here
def transpose(matrix: list):
    new_list = []
    for row in matrix:
         temp = []
         for item in row:
              temp.append(item)
         new_list.append(temp)
#    print(new_list)
    for i in range(len(matrix)):
        #print(matrix[0])
        for j in range(len(matrix[0])):
       
            matrix[i][j] = new_list[j][i]
#    print(matrix)
if __name__ == "__main__":               
    list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

    transpose(list)
    print(list)