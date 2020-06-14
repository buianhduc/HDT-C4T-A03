def gcd(a, b):
    if(a==b): 
        result = a
    elif(a>b): 
        result = gcd(b,a-b)
    else: 
        result = gcd(a,b-a)
    
    return result

print(gcd(100000,32312))
        