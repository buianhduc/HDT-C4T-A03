def fibonacci(number):
    if(number == 1): 
        return 1
    elif(number == 0 ): 
        return 0
    else: 
        return fibonacci(number-1) + fibonacci(number-2)
    
print(fibonacci(6))