import sys
si = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(si())
parent = [i for i in range(0, n + 1)]

points = []
for i in range(n):
    x, y, z = map(int, si().split())
    points.append((x, y, z, i))

edges = []
for i in range(3):
    points.sort(key = lambda x : x[i])
    for j in range(1, n):
        edges.append((abs(points[j - 1][i] - points[j][i]), points[j - 1][3], points[j][3]))
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)