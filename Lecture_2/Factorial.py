def Factorial(num):
    if(num == 0 or num == 1): return 1
    else: return Factorial(num-1)*num

num = int(input("Enter a number: "))
print("Factorial of {0} is {1}".format(num,Factorial(num))) 