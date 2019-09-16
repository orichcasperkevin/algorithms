def minimum_quadratic(list):
    #O(n^2)
    minimum = 0
    for i in list:
        for j in list:
            if i < j:
                minimum = i
    return minimum

def minimum_linear(list):
    #O(n)
    minimum = None
    for i in range(1,len(list)):
        if list[i] < list[i-1]:
            minimum = list[i]
    return minimum

list = [9,7,5,3,2,1]
print(minimum_linear(list))
