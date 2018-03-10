import mergesort
import selection
import copy as c

def merge_median(array):
    n = len(array)
    copy = c.deepcopy(array)
    sorted_array = mergesort.mergeSort(copy)
    if(n % 2 == 0):
        return [sorted_array[n/2-1],sorted_array]
    else:
        return [sorted_array[mergesort.floor_half(n)-1],sorted_array]

def selection_median(array):
    n = len(array)
    copy = c.deepcopy(array)
    if(n % 2 == 0):
        return [selection.selection(n/2-1,copy),copy]
    else:
        return [selection.selection(mergesort.floor_half(n)-1,copy),copy]
