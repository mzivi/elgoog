import math


def selectionsort(array):
    array = array[:]
    result = []
    for i in range(len(array)):
        result.append(array.pop(array.index(min(array))))
    return result


def mergesort(array, implementation="recursive"):

    if implementation.lower() == "recursive":
        _mergesort_recursive(array)
    elif implementation.lower() == "iterative":
        _mergesort_iterative(array)
    else:
        raise "Unknown implementation: {}".format(implementation)


# Implemented using "Divide & Conquer" by recursion
def _mergesort_recursive(array):

    if len(array) < 2:
        return array[:]

    middle = int(0.5 * len(array))

    first_half = _mergesort_recursive(array[:middle])
    second_half = _mergesort_recursive(array[middle:])
    return _merge_sorted(first_half, second_half)


# Implemented using "Divide & Conquer" by explicit loop
def _mergesort_iterative(array):

    sorted_array = array
    h = int(round(math.log(len(array), 2)))
    for i in range(h):
        sorted_array = []
        num_merges = 2**(h - i - 1)
        l = 2**i
        for j in range(num_merges):
            sorted_array += _merge_sorted(array[2 * j * l:2 * j * l + l], array[2 * j * l + l:2 * j * l + 2 * l])
        array = sorted_array
    return sorted_array


def _merge_sorted(array_1, array_2):

    result = []
    i, j = 0, 0
    while i < len(array_1) and j < len(array_2):
        if array_1[i] <= array_2[j]:
            result.append(array_1[i])
            i += 1
        else:
            result.append(array_2[j])
            j += 1

    if i < len(array_1):
        result += array_1[i:]
    if j < len(array_2):
        result += array_2[j:]

    return result


# Implemented using "Divide & Conquer" by recursion
def quicksort(array):

    if len(array) < 2:
        return array[:]

    pivot = _get_pivot(array)
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


def _get_pivot(array):
    return array[0]


if __name__ == '__main__':

    #from random import randint
    #x = [randint(0, 1000000) for i in range(1000)]
    x = [1, 5, 4, 3, 6, 9, 2]
    result = selectionsort(x)
    print(result)
    assert sorted(result) == result
    result = _mergesort_recursive(x)
    print(result)
    assert sorted(result) == result
    result = _mergesort_iterative(x)
    print(result)
    assert sorted(result) == result
    result = quicksort(x)
    print(result)
    assert sorted(result) == result
