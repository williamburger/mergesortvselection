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

def insertion_merge(first, second,count1,count2):
    return_array = []
    i = 0
    j = 0
    overlap = 0
    first.append(MAX)
    second.append(MAX)
    while(len(return_array) != (len(first) + len(second) - 2)):
        if(first[i] <= second[j]):
            return_array.append(first[i])
            i += 1
        else:
            overlap += len(first)-i-1
            return_array.append(second[j])
            j += 1
    return [overlap+count1+count2,return_array]


def count_inversions(array):
    n = len(array)
    half = int(floor_half(n))
    if( n == 0 ):
        count = 0
        return [count,[]]
        
    if( n == 1 ):
        count = 0
        return [count, array]
    else:
       [count1,first] = count_inversions(array = array[0:half])
       [count2,second] = count_inversions(array = array[half:n])
       return insertion_merge(first, second,count1,count2)
