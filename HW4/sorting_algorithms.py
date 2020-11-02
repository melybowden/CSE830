def merge_sort(arr):
    """
    This function will recursively use merge sort to sort the given linked list.
    :param linked_list: an unsorted singly LinkedList
    :param threshold: Use insertion sort when the LinkedList is smaller than or equal to the threshold
    :return: return the sorted linked list
    """
    if arr:
        sz = len(arr)
        if sz <= 1:
            return arr
        list1, list2 = arr[:sz//2], arr[sz//2:]
        list1 = merge_sort(list1)
        list2 = merge_sort(list2)
        arr = merge(list1, list2)
    return arr

def merge(list1, list2):
    """
    This function takes in 2 sorted LinkedLists and merges them together
    :param list1: first sorted list to merge
    :param list2: second sorted list to merge
    :return: one sorted linked list
    """
    sz = len(list1) if list1 else 0
    sz += len(list2) if list2 else 0

    sorted_list = sz*[None]
    i0, i1, i2 = 0, 0, 0
    while list1 and list1 and i1 < len(list1) and i2 < len(list2):
        if list1[i1] < list2[i2]:
            sorted_list[i0] = list1[i1]
            i1 += 1
        else:
            sorted_list[i0] = list2[i2]
            i2 += 1
        i0 += 1
    while list1 and i1 < len(list1):
        sorted_list[i0] = list1[i1]
        i0 += 1
        i1 += 1
    while list2 and i2 < len(list2):
        sorted_list[i0] = list2[i2]
        i0 += 1
        i2 += 1
    return sorted_list

def insertion_sort(arr):
    """
    Sorts an input array in-place using insertion sort O(n^2)
    """
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
    return arr

def tim_sort(arr, threshold=150): #set default threshold based on experiments 1
    if arr: # Could do something clever like determining k based on how many swaps are needed on avg (ie if data seems sorted, keep using insertion sort)
        sz = len(arr)
        if sz <= threshold:
            return insertion_sort(arr)
        list1, list2 = arr[:sz//2], arr[sz//2:]
        list1 = merge_sort(list1)
        list2 = merge_sort(list2)
        arr = merge(list1, list2)
    return arr
