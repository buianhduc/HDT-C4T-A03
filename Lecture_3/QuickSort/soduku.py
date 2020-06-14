def find_first_empty_element(board):
    for i in range(0,10):
        for j in range(0,10):
            if board[i][j] == 0:
                return i,j;
    return None
def valid(board,num,pos):
    # row and column check
    for i in range(len(board[0])):
        if (board[pos[0]][i] == num and pos[1] != i):
            return False
    
    for i in range(len(board)):
        if(board[i][pos[1]] == num and pos[0] != i):
            return False
    #find sub matrix
    #find start points
    startY = pos[1] // 3
    startX = pos[0] // 3
    
    for i in range(startX*3, startX*3+3):
        for j in range(startY*3, startY*3+3):
            if(board[i][j] == num and  [i,j] != pos):
                return False
    
    #return true if all tests passed
    return True

def solve(board):
    find = find_first_empty_element(board)
    if not find:
        return True
    else: 
        row, column = find
    for i in range(1,10):
        if valid(board,i,[row,column]):
            board[row][column] = i
            
            if solve(board):
                return True
            
            board[row][column] = 0
    return False

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -  ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]

solve(board)
print_board(board)