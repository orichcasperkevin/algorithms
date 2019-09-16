import timeit
from timeit import Timer

def bubble_sort(list):
    for pass_num in range(len(list)-1,0,-1):
        for i in range(pass_num):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list


def selection_sort(list):
    for pass_num in range(len(list) -1,0,-1):
        max_pos = 0
        for i in range(1, pass_num + 1):
            if list[i] > list[max_pos]:
                max_pos = i

        list[pass_num], list[max_pos] = list[max_pos], list[pass_num]
    return list

def insertion_sort(list):
    for i in range(1, len(list)):
        curr_value = list[i]
        position = i

        while position > 0 and list[position - 1] > curr_value:
            list[position] = list[position - 1]
            position = position - 1
        list[position] = curr_value

list = [ i for i in range(10,0,-1)]
def bubble():
    bubble_sort(list)
def selection():
    selection_sort(list)

def insertion():
    insertion_sort(list)

t1 = Timer("bubble()", "from __main__ import bubble")
print("bubble sort ",t1.timeit(number=1000), "milliseconds")

t2 = Timer("selection()", "from __main__ import selection")
print("selection ",t2.timeit(number=1000), "milliseconds")

t3 = Timer("insertion()", "from __main__ import insertion")
print("insertion ",t3.timeit(number=1000), "milliseconds")
