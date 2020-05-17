def MinInList(l,currentIndex,currentElement):
    # l is the Initial List
    if(currentIndex == len(l)-2): 
        return currentElement
    elif(currentElement > l[currentIndex+1]):
        currentElement = l[currentIndex+1]
        return MinInList(l,currentIndex+1,currentElement)
    else:
        return MinInList(l,currentIndex+1,currentElement)
    
InitArr = [1,4,-1,4,1,950,24134,439024902]
print(MinInList(InitArr,1,InitArr[0]))