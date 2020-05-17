def MinInList(l,currentIndex):
    # l is the Initial List
    result = l[currentIndex]
    if(currentIndex == len(l)-2): 
        return result
    elif(result > l[currentIndex+1]):
        result = l[currentIndex+1]
        return MinInList(l,currentIndex+1)
    else:
        return MinInList(l,currentIndex+1)
    
InitArr = [1,4,-1,4,1,950,24134,439024902]
print(MinInList(InitArr,0))