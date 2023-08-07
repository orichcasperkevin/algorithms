from array import array


def search(array, el, index=0):
    mid = len(array) // 2    
    if not array:  # Base case: element not found
        return -1

    if array[mid] == el:
        return mid + index

    if el > array[mid]:
        right_sub_array = array[mid+1:]  # Adjust the right sub-array range
        return search(right_sub_array, el, mid + index + 1)

    if el < array[mid]:
        left_sub_array = array[:mid]
        return search(left_sub_array, el, index)


def search_iterative(array,el,index=0):
    mid = len(array) // 2    
    while el != array[mid] :                                
        if el > array[mid]:
            right_sub_array = array[mid+1:]  # Adjust the right sub-array range
            array  = right_sub_array 
            index = mid + index + 1     
            mid = len(array) // 2      
            try:
                array[mid]
            except:
                return -1 
            continue

        if el < array[mid]:
            left_sub_array = array[:mid]
            array = left_sub_array 
            index = index
            mid = len(array) // 2        

            try:
                array[mid]
            except:
                return -1

    return mid + index


# Test the function
arr = [1,2,3,4,5,6,7,8,9,10]
element = 0
result = search_iterative(arr, element)
if result != -1:
    print(f"Element {element} found at index {result}")
else:
    print(f"Element {element} not found in the array")

