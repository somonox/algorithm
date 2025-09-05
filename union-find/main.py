parent = [-1] * 100000

def find(elem):
    if elem < 0:
        return elem
    parent[elem] = find(parent[elem])
    return parent[elem]

def union(elem1, elem2):
    elem1 = find(elem1)
    elem2 = find(elem2)

    if elem1 > elem2:
        parent[elem2] += parent[elem1]
        parent[elem1] = parent[elem2]
    else:
        parent[elem1] += parent[elem2]
        parent[elem2] = parent[elem1]

union(1, 2)
union(3, 1)
print(find(1))
