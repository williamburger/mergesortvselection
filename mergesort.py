# Merge Sort
# William Burger
# Algorithms
# Part of Assigment due march 14th, 2018


MAX = 9999999999

def floor_half(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int((n-1)/2)

def insertion_merge(first, second):
    return_array = []
    i = 0
    j = 0
    first.append(MAX)
    second.append(MAX)
    while(len(return_array) != (len(first) + len(second) - 2)):
        if(first[i] <= second[j]):
            return_array.append(first[i])
            i += 1
        else:
            return_array.append(second[j])
            j += 1
    return return_array


def mergeSort(array):
    n = len(array)
    half = int(floor_half(n))
    if( n == 0 ):
        return []
    if( n == 1 ):
        return array
    else:
       first = mergeSort(array = array[0:half])
       second = mergeSort(array = array[half:n])
       return insertion_merge(first, second)
