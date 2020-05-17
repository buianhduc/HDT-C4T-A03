from math import sqrt

def FindQuadroResults(a,b,c):
    delta = b**2-4*a*c
    
    if(a>0):
        if(delta>0):
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)
            return [x1,x2]
        elif(delta == 0):
            x = (-b)/2*a
            return x
        else:
            return "This equation doesnt have root"
    else: return "This equation doesnt have root"
    
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
print(FindQuadroResults(a,b,c))

    
    
