InitArr =  [1,3,4,16,32,8,64,4,128,2,256,32] #initialize the list
            
dictionary = {}
for index, item in enumerate(InitArr):
    number = item
    InitArr[index] = 0
    for index1, item1 in enumerate(InitArr):
        if number * item1 == 256:
            InitArr[index1] = 0
            dictionary[number] = [number,index,item1,index1]
for values in dictionary.values():
    print('result: {} - index {} and {} - index {}'.format(values[0],values[1],values[2],values[3]))