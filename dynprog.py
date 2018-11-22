def longest_common_substring(string1, string2):
    if len(string1) < 1:
        return ''

    grid = [[int(s == string1[0]) for s in string2]]
    for i in range(1, len(string1)):
        new_grid_row = [int(string1[i] == string2[0])]
        for j in range(1, len(string2)):
            if string1[i] == string2[j]:
                new_grid_row.append(grid[i-1][j-1] + 1)
            else:
                new_grid_row.append(0)
        grid.append(new_grid_row)
    max_lens = [max(r) for r in grid]
    max_len = max(max_lens)
    pos = max_lens.index(max_len)
    return string1[pos-max_len+1:pos+1]


def longest_common_subsequence(string1, string2):
    if len(string1) < 1:
        return ''

    grid = []
    for i in range(len(string1)):
        new_grid_row = []
        for j in range(len(string2)):
            if string1[i] == string2[j]:
                new_grid_row.append(grid[i-1][j-1] + string2[j] if i > 0 and j > 0 else string2[j])
            else:
                prev_up = grid[i-1][j] if i > 0 else ''
                prev_left = new_grid_row[j-1] if j > 0 else ''
                new_grid_row.append(prev_up if len(prev_up) > len(prev_left) else prev_left)
        grid.append(new_grid_row)
    lens = [[len(s) for s in row] for row in grid]
    max_lens = [max(r) for r in lens]
    max_len = max(max_lens)
    idx1 = max_lens.index(max_len)
    idx2 = lens[idx1].index(max_len)
    return grid[idx1][idx2]


def memoized(func):

    cache = {}

    def memo_funct(*args):
        key = tuple(args)
        if key in cache:
            result = cache[key]
        else:
            result = func(*args)
            cache[key] = result
        return result
    return memo_funct


@memoized
def longest_common_subsequence_recursive_1(string1, string2):
    if len(string2) <= 0 or len(string1) <= 0:
        return ''
    if len(string1) > len(string2):
        string1, string2 = string2, string1
    if string1[0] == string2[0]:
        return string1[0] + longest_common_subsequence_recursive_1(string1[1:], string2[1:])
    return longest_common_subsequence_recursive_1(string1, string2[1:])


@memoized
def longest_common_subsequence_recursive_2(string1, string2):
    if len(string2) <= 0 or len(string1) <= 0:
        return ''
    if string2[0] in string1:
        result1 = string2[0] + longest_common_subsequence_recursive_2(string1[string1.index(string2[0]) + 1:], string2[1:])
        result2 = longest_common_subsequence_recursive_2(string1, string2[1:])
        return result1 if len(result1) > len(result2) else result2
    return longest_common_subsequence_recursive_2(string1, string2[1:])


if __name__ == "__main__":

    print(longest_common_substring("fish", "hish"))
    print(longest_common_substring("this is a long string", "this is a short string"))
    print(longest_common_substring("fishfish", "hishhish"))

    print(longest_common_subsequence("fish", "fosh"))
    print(longest_common_subsequence("this is a long string", "this is a short string"))
    print(longest_common_subsequence("fishfish", "hishhish"))

    print(longest_common_subsequence_recursive_1("fish", "fosh"))
    print(longest_common_subsequence_recursive_1("this is a long string", "this is a short string"))
    print(longest_common_subsequence_recursive_1("fishfish", "hishhish"))

    print(longest_common_subsequence_recursive_2("fish", "fosh"))
    print(longest_common_subsequence_recursive_2("this is a long string", "this is a short string"))
    print(longest_common_subsequence_recursive_2("fishfish", "hishhish"))
