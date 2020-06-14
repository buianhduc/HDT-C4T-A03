def initializeMatrix(n):
    a = []
    for i in range(n):
        new = []
        for j in range(n):
            new.append(0)
        a.append(new)
    return a

def find_first_empty_element(board,n):
    for i in range(0,n):
        for j in range(0,n):
            if board[i][j] == 0:
                return [i,j]
    return None

def sumOfRow(arr,row):
    result = 0
    for i in (len(arr)):
        result += arr[row][i]
    return result

def sumOfColumn(arr,column):
    result = 0
    for i in (len(arr)):
        result += arr[i][column]
    return result

def crossSum(arr,left_or_right):
    result = 0
    if left_or_right == True:
        for i in range(len(arr)):
            result += arr[i][i]
    else:
        for i in range(len(arr)-1,-1,-1): 
            result += arr[i][i]
    return result    

def valid(arr,num,pos):
    initialSum = sumOfRow(arr,0)
    for i in range(1,len(arr)):
        if sumOfRow(arr,i) != initialSum or sumOfColumn(arr,i) != initialSum:
            return False
    if crossSum(arr,True) != initialSum or crossSum(arr,False) != initialSum:
        return False
    return True

def solve(arr,n):
    find = find_first_empty_element(arr,n)
    if len(find)==0: 
        return True
    
    row,col = find[0],find[1]
    
    for i in range(1,n+1):
        if valid(arr,i,[row,col]):
            arr[row][col] = i
            
            if solve(arr,n):
                return True
        
            arr[row][col] = 0
    return False
arr = initializeMatrix(3)
solve(arr,3)
print(arr)