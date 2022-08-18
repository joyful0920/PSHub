import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
e = int(si())
graph = [deque() for _ in range(n + 1)]

for _ in range(e):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = deque()
    visited.append(start)
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    print(len(visited) - 1)

bfs(1)