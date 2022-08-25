# import sys
from collections import deque
# sys.stdin = open('input.txt')


def bfs(x, y):
    q = deque([(x, y)])     # 큐에 일단 시작점 넣고
    visited[x][y] = True    # 방문 처리까지

    while q:                # 큐에 원소가 있는 동안 반복
        x, y = q.popleft()  # 위치 하나 뽑고
        for i in range(4):  # 델타 탐색으로 인접한 주변 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]                  # 범위내 & 미방문 & 벽이 아니고
            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and maze[nx][ny] != 1:
                if maze[nx][ny] == 3:       # 도착점이면 1 리턴
                    return 1
                else:                       # 도착점이 아닌 통로라면
                    q.append((nx ,ny))      # 해당 위치 큐에 삽입
                    visited[nx][ny] = True  # 방문 처리  

    return 0    # 도달 불가능하면 0 리턴


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:     # 출발점에서 BFS 수행
                result = bfs(i, j)

    print(f'#{tc} {result}')
