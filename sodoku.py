board = [[0,8,0,4,0,5,0,9,0],
[3,0,0,9,0,0,0,1,0],
[0,0,5,0,6,3,7,4,0],
[8,0,3,0,5,7,0,2,1],
[0,5,0,1,0,4,3,8,7],
[0,0,0,3,0,0,0,0,4],
[4,0,0,0,2,0,1,8,0],
[0,0,6,1,9,0,0,0,5],
[0,0,0,8,0,0,0,7,9]]

def valid_placement(row,col,value,board):
    if value in board[row]:
        return False
    column = []
    for i in range(len(board)):
        column.append(board[i][col])
    if value in column:
        return False
    if 0<=row<=2:
        if 0<=col<=2:
            if value in board[0][0:3] or value in board[1][0:3] or value in board[2][0:3]:
                return False
        if 3<=col<=5:
            if value in board[0][3:6] or value in board[1][3:6] or value in board[2][3:6]:
                return False
        if 6<=col<=8:
            if value in board[0][6:] or value in board[1][6:] or value in board[2][6:]:
                return False
    if 3<=row<=5:
        if 0<=col<=2:
            if value in board[3][0:3] or value in board[4][0:3] or value in board[5][0:3]:
                return False
        if 3<=col<=5:
            if value in board[3][3:6] or value in board[4][3:6] or value in board[5][3:6]:
                return False
        if 6<=col<=8:
            if value in board[3][6:] or value in board[4][6:] or value in board[5][6:]:
                return False
    if 6<=row<=8:
        if 0<=col<=2:
            if value in board[6][0:3] or value in board[7][0:3] or value in board[8][0:3]:
                return False
        if 3<=col<=5:
            if value in board[6][3:6] or value in board[7][3:6] or value in board[8][3:6]:
                return False
        if 6<=col<=8:
            if value in board[6][6:] or value in board[7][6:] or value in board[8][6:]:
                return False
    return True


def solve(row, col, board):

    for number in range(1,10):

        if valid_placement(row, col, number,board):
            board[row][col] = number
            break

    return board

def solve_board(board):

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                board = solve(row,col,board)
    for row in board:
        print(row)

solve_board(board)
        

