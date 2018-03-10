# Selection 
# William Burger
# Algorithms
# Part of Assigment due march 14th, 2018

def partition(array):
    p = array[0]
    k = 0
    low = 1 
    high = len(array)-1
    if len(array) == 2:
        if(array[0]<=array[1]):
            return 0
        else:
            tmp = array[0]
            array[0] = array[1]
            array[1] = tmp
            return 1 
        
    while(low<high):
        while(low <= len(array)-1 and array[low] <= p):
            low += 1 
        while(high > 0 and array[high] > p ): 
            high -= 1
            
        if(high>low):
            tmp = array[low]
            array[low] = array[high]
            array[high] = tmp
    tmp = array[0]
    array[0] = array[high]
    array[high] = tmp
    return high

def selection(m, array):
    k  = partition(array)
    if( m == k):
        return array[k]
    elif( m < k ):
        return selection( m, array[0:k]) 
    else:
        return selection( m-k-1, array[k+1:len(array)])
