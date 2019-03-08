import heapq


def percentile(array, k):

    if len(array) <= k:
        return sorted(array)

    heap = [-n for n in array[:k]]
    heapq.heapify(heap)
    for n in array[k:]:
        if n < - heap[0]:
            heapq.heapreplace(heap, -n)
    return - heap[0]


if __name__ == '__main__':

    print(percentile([1, 7, 8, 2, 3, 10, 9, 4, 6, 5], 1))
    print(percentile([1, 7, 8, 2, 3, 10, 9, 4, 6, 5], 2))
    print(percentile([1, 7, 8, 2, 3, 10, 9, 4, 6, 5], 3))
    print(percentile([1, 7, 8, 2, 3, 10, 9, 4, 6, 5], 4))
    print(percentile([1, 7, 8, 2, 3, 10, 9, 4, 6, 5], 5))
    print(percentile([1, 7, 8, 2, 3, 10, 9, 4, 6, 5], 6))
    print(percentile([1, 7, 8, 2, 3, 10, 9, 4, 6, 5], 7))
