from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque([(x, y, 1)])

    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] + 1:
                q.append((nx, ny, d + 1))

    return d


for tc in range(1, int(input()) + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    max_depth = 0
    for i in range(n):
        for j in range(n):
            depth = bfs(i, j)
            if depth == max_depth and graph[i][j] < result:
                result = graph[i][j]
            if depth > max_depth:
                max_depth = depth
                result = graph[i][j]

    print(f'#{tc} {result} {max_depth}')