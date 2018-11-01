def selection_sort(x):
    result = []
    for i in range(len(x)):
        result.append(x.pop(x.index(min(x))))
    return result


if __name__ == '__main__':
    print(selection_sort([1, 2, 5, 4, 6, 3]))
