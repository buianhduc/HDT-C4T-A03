InitArr =  [1,3,4,16,32,8,64,4,128,2,256,32] #initialize the list
for i in range(len(InitArr)): 
    for j in range(i+1,len(InitArr)):
        
        if(InitArr[i]*InitArr[j]==256): #check if mutipling two elements equals 256
            print("{0} x {1} at the positions {2} and {3}, respectively".format(InitArr[i],InitArr[j],i+1,j+1)) #print