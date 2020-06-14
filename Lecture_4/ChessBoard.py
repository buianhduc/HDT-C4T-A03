n = 6
def print_solution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def solveKT():
    # Initialization of Board matrix  
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
    ]

    # move_x and move_y define next move of Knight.  
    # move_x is for next value of x coordinate  
    # move_y is for next value of y coordinate 
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # First place of Knight 
    board[0][0] = 0

    # Step counter for knight's position 
    pos = 1

    # Checking if solution exists or not  
    if (not solveKT_util(board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        print_solution(board)

def isSafe(x,y,board):
    if(x >= 0 and y >= 0 and x<n and y<n and board[x][y] == -1): 
        return True
    return False

def solveKT_util(board, curr_x, curr_y, move_x, move_y, pos):
    if (pos == n ** 2):
        return True
    for i in move_x:
        for j in move_y:
            new_x = curr_x + i
            new_y = curr_y + j
            if isSafe(new_x, new_y,board):
                board[new_x][new_y] = pos
                if  solveKT_util(board, new_x, new_y, move_x, move_y, pos+1): 
                    return True
                board[new_x][new_y] = -1
    return False

solveKT()