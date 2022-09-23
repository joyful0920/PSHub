from heapq import heappush

dx = [
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1]
]

dy = [
    [1, -1],
    [-1, -1],
    [-1, 1],
    [1, 1]
]


def dfs(x, y, visited, cnt, di):
    if len(visited) == 1 and x == start[0] and y == start[1]:
        nx = x + dx[di][0]
        ny = y + dy[di][0]
        if cafe[nx][ny] not in visited:
            visited.append(cafe[nx][ny])
            dfs(nx, ny, visited, cnt + 1, di)
        return

    for i in range(2):
        nx = x + dx[di][i]
        ny = y + dy[di][i]
        if 0 <= nx < n and 0 <= ny < n:
            if nx == start[0] and ny == start[1]:
                heappush(result, (-cnt, cnt))
                return
            if cafe[nx][ny] not in visited:
                visited.append(cafe[nx][ny])
                if di + i < 4:
                    dfs(nx, ny, visited, cnt + 1, di + i)
                visited.pop()


for tc in range(1, int(input()) + 1):
    n = int(input())
    cafe = [list(map(int, input().split())) for _ in range(n)]

    result = [(1, -1)]
    for i in range(n - 2):
        for j in range(1, n - 1):
            start = (i, j, cafe[i][j])
            dfs(start[0], start[1], [start[2]], 1, 0)

    print(f'#{tc} {result[0][1]}')