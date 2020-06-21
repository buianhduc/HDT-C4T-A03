import math
#Bai 1
def question1(n):
    result = 0
    while (n > 0): 
        k = int(n) % 10
        result += k
        n = int(n/10)
    return result

#Bai 2
def question2(n):
    if(n == 0):
        return 0
    return n+question2(n-1)


#Bai 3
def question3(n,s = 0):
    i = 0
    while(n != 0): 
        s += (n % 2)*pow(10,i)
        n = n // 2
        i += 1
    return s
#Bai 4
def question4(maze = [  [1, 0, 0, 0], 
                        [1, 1, 0, 1], 
                        [0, 1, 0, 0], 
                        [1, 1, 1, 1]]):
    def print_board():
        for i in range(len(maze)):
            for j in range(len(maze)):
                print(maze[i][j],end = " ")
            print()
        print()
    
    def nextMove(x,y):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        validNextMove = []
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if (new_x > 0 and new_y > 0 and new_x < len(maze) and new_y < len(maze)):
                if(maze[new_x][new_y] == 1): 
                    validNextMove.append([new_x,new_y])
        return validNextMove
    
    def solveMaze(pos):
        x = pos[0]
        y = pos[1]
        
        if(x==y and x==len(maze)-1):
            return True
        next_move = nextMove(x,y)
        
        for move in next_move:
            new_x = move[0]
            new_y = move[1]

            currentVal = maze[new_x][new_y]
            maze[new_x][new_y] = 2
            if solveMaze(move):
                return True
            maze[new_x][new_y] = currentVal
        return False   
    
    def printSolution():
        maze[0][0] = 2
        if solveMaze([0,0]):
            print_board()
            return "solved"
        else:
            return "cannot be solved"
    
    print(printSolution())


def question5(startPos,endPos):
    x,y = startPos
    dx,dy = endPos
    
    if(x == dx and y == dy):
        return True
    elif(x*y > 0 and (abs(x) > abs(dx) or abs(y) > abs(dy))):
        return False
    elif(x == y and y == 0): 
        return False
    elif(x == 0): 
        return question5([x+y,y],endPos)
    elif(y == 0): 
        return question5([x,y+x],endPos)
    
    return (question5([x,x+y],endPos) or question5([x+y,y],endPos))
#Bai 6
def question6(n):
    if (n == 0): return 0;
    for i in range(1,n):
        lower = math.floor(i*(i+1)/2);
        upper = math.floor((i+1)*(i+2)/2);
        if (lower <= n and n <= upper):
            return min(i + 2 * (n-lower),i+1+ 2 * (upper-n))

print(question6(3))