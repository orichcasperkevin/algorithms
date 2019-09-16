import timeit
from timeit import Timer


def concat_list():
    # O(k) where k is the size of list being concatenated
    l = []
    for i in range(1000):
        l = l + [i]

def append_list():
    l = []
    for i in range(1000):
        l.append(i)

def list_comprehension():
    l = [i for i in range(1000)]

def list_function_call():
    l = list(range(1000))


t1 = Timer("concat_list()", "from __main__ import concat_list")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("append_list()", "from __main__ import append_list")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("list_comprehension()", "from __main__ import list_comprehension")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("list_function_call()", "from __main__ import list_function_call")
print("list range ",t4.timeit(number=1000), "milliseconds")
