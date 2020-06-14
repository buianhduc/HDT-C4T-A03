def merge_sort(arr):
    if(len(arr) <= 1): 
        return arr
    
    mid = len(arr) // 2
    
    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])
    
    return merge(left_list, right_list)

def merge(left_list, right_list, result = []):
    
    if(left_list[0] > right_list[0]): 
        result.append(right_list[0])
        right_list.pop(0)
    else: 
        result.append(left_list[0])
        left_list.pop(0)
    merge(left_list, right_list, result)
    return result
arr = [2,22,92,1,13,24]
print(merge_sort(arr))