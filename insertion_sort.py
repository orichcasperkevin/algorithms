def insertionSort(array):
    sorted_array = []
    for i,item in enumerate(array):        
        sorted_array.append(item)        
        j = i
        while j >= 1 and sorted_array[j-1] > sorted_array[j]:            
            sorted_array[j-1],sorted_array[j] = sorted_array[j],sorted_array[j-1]            
            j -= 1           
    return sorted_array

def mergeSort(array):    
    def merge(left, right):
        merged_list = []
        left_index, right_index = 0, 0

        # Merge the two halves by comparing elements
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged_list.append(left[left_index])
                left_index += 1
            else:
                merged_list.append(right[right_index])
                right_index += 1

        # Append any remaining elements from the left and right halves
        merged_list.extend(left[left_index:])
        merged_list.extend(right[right_index:])
        return merged_list

    def sort(arr):
        if len(arr) <= 1:
            return arr

        # Divide the array into two halves
        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]

        # Recursively sort each half
        left_half = sort(left_half)
        right_half = sort(right_half)

        # Merge the sorted halves
        return merge(left_half, right_half)
    
    return sort(array)
    
def sortedArrays(nums1,nums2):
    combined_array = nums1 + nums2
    # sorted_merged_array = insertionSort(combined_array)
    # print(sorted_merged_array)
    sorted_merged_array = mergeSort(combined_array)
    print(sorted_merged_array)

sortedArrays([9,8,7,6],[5,4,3,2])
# sortedArrays([2],[])