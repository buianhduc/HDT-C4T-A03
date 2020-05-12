# def SortedOrNot(arr):
#     a = True
#     for i in range(0,len(arr)-2):
#         if(arr[i]>arr[i+1]):
#             a = False
#             break
#     return a

def bubble_sort(a):
    for i in range(0,len(a)-2):
        for j in range(1,len(a)-1):
            if(a[i]<a[j]):
                a[i],a[j]=a[j],a[i]
            print(a[i])
        # if(SortedOrNot(a)): 
        #     break

arr = [4,5,1,8,9,10,5,6,4,3]


for i in range(0,3):
    print("{0} ".format(arr[i]), end = '')
print("\n")


for i in range(0,3):
    print("{0} ".format(arr[len(arr)-1-i]), end='')
print("\n")
    
bubble_sort(arr)
for i in arr:
    print("{0} ".format(i),end='')
print("\n")

for i in range(len(arr)):
    print("{0}".format(arr[len(arr)-i-1]), end=' ')
print("\n")
#split slicing a[a:b] 

#person['sex'] = person.pop('gender')
