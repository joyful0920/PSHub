import sys

# sys.stdin = open('input.txt')
si = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(x, y):
    # 현재 위치가 범위 내 & 미방문 & 배추 존재
    if 0 <= x < n and 0 <= y < m and not visited[x][y] and graph[x][y] == 1:
        visited[x][y] = True                    # 방문 처리
        for di in range(4):                     # 주위 네 방향에 대해
            dfs(x + dx[di], y + dy[di])         # 재귀적으로 DFS 수행

        return True                             # 모든 재귀가 끝나면 True 리턴


dx = [1, -1, 0, 0]                              # 델타 탐색 방향 리스트
dy = [0, 0, 1, -1]

t = int(si())
for _ in range(t):
    m, n, k = map(int, si().split())            # 가로, 세로, 배추 개수

    graph = [[0] * m for _ in range(n)]         # 인접 행렬 0으로 초기화 (2차원)
    visited = [[False] * m for _ in range(n)]   # visited 리스트 (2차원)

    for _ in range(k):
        X, Y = map(int, si().split())           # 배추 위치
        graph[Y][X] = 1                         # 그래프에서 1로 업뎃

    cnt = 0                                     # 지렁이 카운트 변수
    for i in range(n):                          # 그래프의 모든 위치에 대해 DFS
        for j in range(m):
            if dfs(i, j):                       # DFS 리턴값이 True
                cnt += 1                        # 하나의 배추 구역 DFS 수행 완료

    print(cnt)
