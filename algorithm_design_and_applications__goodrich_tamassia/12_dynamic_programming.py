def longest_common_subsequence(s1, s2):
    L = []
    for i in range(len(s1)):
        Li = []
        L.append(Li)
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                Lij = 1 + L[i - 1][j - 1] if i > 0 and j > 0 else 1
            else:
                Lij = max(L[i][j - 1] if j > 0 else 0, L[i - 1][j] if i > 0 else 0)
            Li.append(Lij)
    s = []
    i = len(s1) - 1
    j = len(s2) - 1
    while i >= 0 and j >= 0:
        if s1[i] == s2[j]:
            s.append(s1[i])
            i -= 1
            j -= 1
        else:
            Lup = L[i - 1][j] if i > 0 else 0
            Llf = L[i][j - 1] if j > 0 else 0
            if Lup >= Llf:
                i -= 1
            else:
                j -= 1

    return ''.join(reversed(s))


def knapsack(items, weight):
    benefits = [item[0] for item in items]
    weights = [item[1] for item in items]
    B = []
    for w in range(weight + 1):
        Bw = [benefits[0] if weights[0] <= w else 0]
        B.append(Bw)
        for i in range(1, len(items)):
            if weights[i] > w:
                Bwi = B[w][i - 1]
            else:
                Bwi = max(B[w][i - 1], B[w - weights[i]][i - 1] + benefits[i])
            Bw.append(Bwi)

    i = len(items) - 1
    w = weight
    ks = []
    while i > 0:
        if B[w][i] > B[w][i - 1]:
            ks.append(items[i])
            w -= weights[i]
        i -= 1
    if weights[0] <= w:
        ks.append(items[0])

    return list(reversed(ks))


if __name__ == '__main__':

    print(knapsack([(3, 2), (5, 4), (8, 5), (4, 3), (10, 9)], 20))
    print(longest_common_subsequence('xyxxyzzzxzyx', 'xxyzzxx'))
