import timeit
from timeit import Timer

def sequential_search(search_item,list):
    for item in list:
        if item == search_item:
            return True
    return False

def sequential_search_ordered_list(search_item,list):
    for item in list:
        if item > search_item :
            return False
        if item == search_item:
            return True
    return False

def binary_search(search_item,list):
    pivot = len(list) // 2

    if len(list) == 1 and list[0] != search_item :
        return False
    else:
        if list[pivot] == search_item:
            return True
        if list[pivot] > search_item:
            return binary_search(search_item,list[:pivot])
        if list[pivot] < search_item:
            return binary_search(search_item,list[pivot:])


def binary_search_it(search_item, list):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == search_item:
            return True
        else:
            if search_item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return False



list = [ i for i in range(100000)]
def bin():
    binary_search(100000,list)
def bin_it():
    binary_search_it(100000,list)
def seq():
    sequential_search_ordered_list(100000,list)

t1 = Timer("bin()", "from __main__ import bin")
print("binary search ",t1.timeit(number=1000), "milliseconds")

t2 = Timer("bin_it()", "from __main__ import bin_it")
print("bin_it1 ",t2.timeit(number=1000), "milliseconds")

t3 = Timer("seq()", "from __main__ import seq")
print("seq ",t3.timeit(number=1000), "milliseconds")
