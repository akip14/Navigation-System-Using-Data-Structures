import numpy as np

def heapify(heapArray, numItems):
    #Start at the last non-leaf node and go backwards
    for ii in range(numItems // 2 - 1, -1, -1):
        trickleDown(heapArray, ii, numItems)

def trickleDown(heapArray, ii, numItems):
    smallest = ii
    left =  2*ii + 1
    right = 2*ii + 2

    # find the largest element among the parent and its children
    if left < numItems and heapArray[left][0] < heapArray[smallest][0]:
        smallest = left

    if right < numItems and heapArray[right][0] < heapArray[smallest][0]:
        smallest = right

    # Swap the parent with the largest child and trickle down  
    if smallest != ii:
        heapArray[ii], heapArray[smallest] = heapArray[smallest], heapArray[ii]
        trickleDown(heapArray, smallest, numItems)

def heapSort(arr, numItems):
    heapify(arr, numItems)
    for ii in range(numItems - 1, 0, -1):
        # Swap the root with the last element and trickle down
        temp  = arr[0]
        arr[0] = arr[ii]
        arr[ii] = temp
        trickleDown(arr, 0, ii)
    
    return arr



