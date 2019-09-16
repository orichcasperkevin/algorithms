def minimum_linear(list):
    #O(n)
    minimum = None
    for i in range(1,len(list)):        
        if list[i] < list[i-1]:
            minimum = list[i]
    return minimum

def kth_minimum_linear(list,k):
    cur_list = list
    count = 1
    while(count <= k ):
        minimum = minimum_linear(cur_list)
        cur_list.remove(minimum)
        count += 1
    return minimum

list = [9,7,5,3,2,1]
print(kth_minimum_linear(list,5))
