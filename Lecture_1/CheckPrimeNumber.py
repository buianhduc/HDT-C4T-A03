def CheckPrimeNumber(a):
    if(a<2): return False
    if(a>2):
        if(a%2==0): return False
        if(a%3==0): return False
        i = 5
    while(i * i <= a) : 
        if (a % i == 0 or a % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

numInp = int(input("Enter a number: ")) #input
if(CheckPrimeNumber(numInp)): print("{0} is a prime number".format(numInp))
else: print("{0} is not a prime number".format(numInp)) #output