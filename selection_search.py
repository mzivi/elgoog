def selection_search(x):
    result = []
    for i in range(len(x)):
        result.append(x.pop(x.index(max(x))))
    return result


if __name__ == '__main__':
    print(selection_search([1, 2, 5, 4, 6, 3]))
