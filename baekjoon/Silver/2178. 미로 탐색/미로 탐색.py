import sys
from collections import deque
# sys.stdin = open('input.txt')
si = sys.stdin.readline

dx = [-1, 1, 0, 0]  # 델타 탐색 리스트
dy = [0, 0, -1, 1]


def bfs(x, y):                                  # BFS 함수
    visited = [[False] * m for _ in range(n)]   # 방문 처리 리스트
    visited[x][y] = True                        # 시작 지점 방문 처리
    q = deque([(x, y, 1)])                      # 큐에 시작점 위치와, 이동 칸 수 튜플로 묶어 삽입

    while q:                                    # 큐에 원소가 있는 동안
        x, y, dist = q.popleft()                # 원소 하나를 팝
        if x == n - 1 and y == m - 1:           # 도착 점이라면
            return dist                         # 이동 칸 수 반환
        for i in range(4):                      # 인접 4 방향에 대해
            nx = x + dx[i]                      # 다음 이동 위치 세팅
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == '1':
                visited[nx][ny] = True          # 범위 내 & 미방문 & 1인 칸만 이동 가능
                q.append((nx, ny, dist + 1))    # 이동 가능한 위치를 이동 칸 수 + 1 하여 큐에 삽입


n, m = map(int, si().split())
maze = [si() for _ in range(n)]

print(bfs(0, 0))
