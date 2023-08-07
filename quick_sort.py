def quicksort(list):
    pivot = len(list)-1
    largest_pointer = 0
    current = 0

    while current <= pivot:
        print(list[current],list[largest_pointer])
        if list[current] >= list[pivot]:
            list[pivot],list[current] = list[current],list[pivot]

        if list[current] < list[largest_pointer]:
            list[largest_pointer],list[current] = list[current],list[largest_pointer]
            largest_pointer = current
        current += 1
        print(list,largest_pointer)


quicksort([10,9,8,7,6,5,4,3,2,1])