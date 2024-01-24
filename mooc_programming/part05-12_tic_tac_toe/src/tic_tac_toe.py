# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    # x = col
    # y = y
    # Checking conditions for an invalid input:
    # invalid coordinates
    if x > 2 or x < 0 or y > 2 or y < 0:
        return False
    # invalid piece
    if piece.lower() != 'x' and piece.lower() != 'o':
        return False
    # Space is occupied 
    if game_board[y][x] != '':
        return False

            
    game_board[y][x] = piece
    return True
#    0    1   2
#ame_board = [
#    ["", "", ""], 
#    ["", "", ""], #[['', 'x']]
#    ["", "", ""]]
#game_board = [
#    [['', '', 'X'], ['', '', ''], ['', 'O', '']]#, 0, 0, X
#]
#game_board = [['', '', 'O'], ['O', '', 'X'], ['', 'O', '']] #, 1, 1, O
#game_board = [['X', '', ''], ['', '', ''], ['O', '', 'O']]#, 0, 0, X
#game_board = [['', '', 'O'], ['', '', 'O'], ['', 'X', 'O']]#,# 0, 0, X
#print(play_turn(game_board, 0, 0, 'X'))
#print(play_turn(game_board, 0, 0, 'X'))
#print(play_turn(game_board, 1, 1, "O"))
#print(play_turn(game_board, 0, 0, "X"))
#print(play_turn(game_board, 2, 0, "X"))
#print(game_board)
#[[0, '', 'X'], ['', '', ''], ['', 'O', '']] != [['X', '', 'X'], ['', '', ''], ['', 'O', '']]