from math import floor


def selectionsort(array):

    for i in range(len(array)):
        leftover = array[i:]
        min_idx = leftover.index(min(leftover))
        array[i], array[i + min_idx] = array[i + min_idx], array[i]


def insertionsort(array):

    for i in range(1, len(array)):
        x = array[i]
        j = i - 1
        while j >= 0 and array[j] > x:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = x


def quicksort(array, implementation="recursive"):

    if implementation.lower() == "recursive":
        _quicksort_recursive(array, 0, len(array) - 1)
    elif implementation.lower() == "iterative":
        _quicksort_iterative(array)
    else:
        raise "Unknown implementation: {}".format(implementation)


def _quicksort_recursive(array, first_idx, last_idx):

    if first_idx >= last_idx:
        return

    left, right = first_idx, last_idx
    pivot = left
    while left < right:
        if left < pivot:
            if array[left] <= array[pivot]:
                left += 1
            else:
                array[left], array[pivot] = array[pivot], array[left]
                pivot = left
        else:  # pivot == left
            if array[right] >= array[pivot]:
                right -= 1
            else:
                array[right], array[pivot] = array[pivot], array[right]
                pivot = right
    _quicksort_recursive(array, first_idx, pivot - 1)
    _quicksort_recursive(array, pivot + 1, last_idx)


def _quicksort_iterative(array):

    if len(array) < 2:
        return

    index_stack = [0, len(array) - 1]
    while len(index_stack) > 0:
        last_idx = index_stack.pop()
        first_idx = index_stack.pop()
        left, right = first_idx, last_idx
        pivot = left
        while left < right:
            if left < pivot:
                if array[left] <= array[pivot]:
                    left += 1
                else:
                    array[left], array[pivot] = array[pivot], array[left]
                    pivot = left
            else:  # pivot == left
                if array[right] >= array[pivot]:
                    right -= 1
                else:
                    array[right], array[pivot] = array[pivot], array[right]
                    pivot = right
        if first_idx < pivot - 1:
            index_stack += [first_idx, pivot - 1]
        if last_idx > pivot + 1:
            index_stack += [pivot + 1, last_idx]


def heapsort(array):
    _build_heap(array)
    _sort_heap(array)


def _build_heap(array):

    for i in range(1, len(array)):
        _up_heap(array, i)


def _up_heap(heap, new_idx):
    parent_idx = (new_idx - 1) // 2
    while parent_idx >= 0 and heap[parent_idx] < heap[new_idx]:
        heap[parent_idx], heap[new_idx] = heap[new_idx], heap[parent_idx]
        new_idx = parent_idx
        parent_idx = (new_idx - 1) // 2


def _sort_heap(heap):
    for i in range(len(heap) - 1, 0, -1):
        _down_heap(heap, i)


def _down_heap(heap, last_idx):

    if last_idx < 1:
        return

    heap[0], heap[last_idx] = heap[last_idx], heap[0]
    parent_idx = 0
    while True:
        child_idx = 2 * parent_idx + 2  # start from the right child
        if child_idx < last_idx:
            if heap[child_idx - 1] > heap[child_idx]:  # left child is bigger
                child_idx -= 1
        else:  # there is no right child to this node
            child_idx -= 1  # check the left index
        if child_idx < last_idx and heap[parent_idx] < heap[child_idx]:
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
            parent_idx = child_idx
        else:
            break


def dheapsort(array, d):
    _build_d_heap(array, d)
    _sort_d_heap(array, d)


def _build_d_heap(array, d):

    for i in range(1, len(array)):
        _up_d_heap(array, d, i)


def _up_d_heap(heap, d, new_idx):
    parent_idx = (new_idx - 1) // d
    while parent_idx >= 0 and heap[parent_idx] < heap[new_idx]:
        heap[parent_idx], heap[new_idx] = heap[new_idx], heap[parent_idx]
        new_idx = parent_idx
        parent_idx = (new_idx - 1) // d


def _sort_d_heap(heap, d):
    for i in range(len(heap) - 1, 0, -1):
        _down_d_heap(heap, d, i)


def _down_d_heap(heap, d, last_idx):

    if last_idx < 1:
        return

    heap[0], heap[last_idx] = heap[last_idx], heap[0]
    parent_idx = 0
    largest_idx = parent_idx
    while True:
        for i in range(d):
            child_idx = d * (parent_idx + 1) - i  # start from the right child
            if child_idx < last_idx and heap[largest_idx] < heap[child_idx]:
                largest_idx = child_idx
        if parent_idx != largest_idx:
            heap[parent_idx], heap[largest_idx] = heap[largest_idx], heap[parent_idx]
            parent_idx = largest_idx
        else:
            break


if __name__ == "__main__":

    x = [1, 5, 4, 3, 7, 6, 2]

    xx = x[:]
    insertionsort(xx)
    print(xx)
    assert sorted(xx) == xx
    xx = x[:]
    selectionsort(xx)
    print(xx)
    assert sorted(xx) == xx
    xx = x[:]
    quicksort(xx)
    print(xx)
    assert sorted(xx) == xx
    xx = x[:]
    quicksort(xx, implementation="iterative")
    print(xx)
    assert sorted(xx) == xx
    xx = x[:]
    heapsort(xx)
    print(xx)
    assert sorted(xx) == xx
    xx = x[:]
    dheapsort(xx, 3)
    print(xx)
    assert sorted(xx) == xx
