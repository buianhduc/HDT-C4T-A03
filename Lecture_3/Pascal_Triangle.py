def Factorial(num):
    if(num == 0 or num == 1): return 1
    else: return Factorial(num-1)*num
def Pascal_triangle(row):
    for i in range(0,row): 
        for j in range(0,row-i-1): 
            print(' ',end='')
        for j in range(0,i):
            print(Factorial(i)/Factorial(j)*Factorial(i-j))


print(Pascal_triangle(10))    