import sys
from collections import deque
# sys.stdin = open('input.txt')
si = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]    # 델타 탐색 리스트
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():                                  # BFS 함수
    q = deque([])
    for k in range(h):                      # 토마토 상자를 전체 탐색
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 1:    # 익은 토마토가 있다면
                    q.append((k, i, j, 0))  # 일단 큐에 토마토 위치와 익는 데 걸린 날을 0으로 묶어 추가

    max_day = 0                     # 토마토가 익는 데 걸린 최장일
    while q:                        # 큐에 원소가 있는 동안
        z, x, y, day = q.popleft()  # 원소 하나를 팝
        if day > max_day:           # 현재 최장일보다 큰 day라면
            max_day = day           # max_day 업뎃
        for i in range(6):          # 델타 탐색 리스트로 다음 위치 세팅
            nx, ny, nz = x, y, z
            if 0 <= i < 4:
                nx += dx[i]
                ny += dy[i]
            else:
                nz += dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = 1              # 범위 내 & 안 익은 토마토라면 익히기
                q.append((nz, nx, ny, day + 1))     # 방금 익은 토마토의 위치와 걸린 일 수를 큐에 저장

    return max_day  # BFS 수행 후 최장일 리턴


m, n, h = map(int, si().split())
tomato = [[list(map(int, si().split())) for _ in range(n)] for _ in range(h)]

result = bfs()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 0:    # 안익은 토마토가 있다면
                result = -1             # 결과값은 -1
                break

print(result)