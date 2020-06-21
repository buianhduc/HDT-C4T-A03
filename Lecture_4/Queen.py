n = 5

def print_solution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def printBoard(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def isSafe(row, col, board): 
  
    # Check this row on left side 
    for i in range(col): 
        if board[row][i] == 1: 
            return False
  
    # Check upper diagonal on left side 
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    # Check lower diagonal on left side 
    for i, j in zip(range(row, n, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True

def solve():
    board = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]
    
    if(not SolveQ_unti(board,0)):
        print("Unavailable Solution")
    else:
        printBoard(board)

def SolveQ_unti(board,pos):
    if pos == 5:
        return True
    for i in range(n):
            if(isSafe(i,pos,board)):
                board[i][pos] = 1
                if(SolveQ_unti(board,pos+1)):
                    return True
                board[i][j] == 0
    return False

solve()
