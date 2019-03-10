# Minimum Spanning Trees (MST)


def kruskal(vertices, edges):
    result = []
    subsets = {v: set([v]) for v in vertices}
    sorted_edges = sorted([(w, e) for e, w in edges.items()])
    for w, e in sorted_edges:
        s1 = subsets[e[0]]
        s2 = subsets[e[1]]
        if s1 is not s2:
            result.append(e)
            s1.update(s2)
            if len(s1) == len(vertices):
                break
            for v in s2:
                subsets[v] = s1
    return result


if __name__ == '__main__':

    vertices = [1, 2, 3, 4, 5]
    edges = {
        (1, 2): 1.0, (2, 1): 1.0,
        (1, 3): 0.4, (3, 1): 0.4,
        (2, 3): 1.0, (3, 2): 1.0,
        (2, 4): 0.2, (4, 2): 0.2,
        (3, 5): 0.5, (3, 5): 0.5,
        (4, 5): 0.8, (4, 5): 0.8
    }
    print(kruskal(vertices, edges))
