import sys

# sys.stdin = open('input.txt')
si = sys.stdin.readline


def dfs(x, y):                                      # DFS 함수
                                                    # 그래프 내 범위 & 집 존재 & 미방문한 곳이라면
    if 0 <= x < n and 0 <= y < n and graph[x][y] == '1' and not visited[x][y]:
        global cnt
        cnt += 1                                    # 현재 단지의 집 수 +1
        visited[x][y] = True                        # 방문 처리
        for di in range(4):                         # 델타 탐색으로 인접한 집 확인
            dfs(x + dx[di], y + dy[di])             # 인접 좌표로 재귀적 DFS 수행

        return True                                 # 한 단지 계산이 끝나면 리턴 True


dx = [1, -1, 0, 0]                                  # 방향 인덱스 리스트
dy = [0, 0, 1, -1]

n = int(si())
graph = [si().rstrip() for _ in range(n)]           # 인접 행렬 graph
visited = [[False] * n for _ in range(n)]           # visited 리스트

cnts = []                                           # 각각 단지내의 집 수를 저장할 cnts 리스트
for i in range(n):                                  # graph를 완전 탐색하며 DFS 수행
    for j in range(n):
        cnt = 0                                     # 단지내 집 수 0으로 초기화
        if dfs(i, j):                               # dfs의 리턴이 True => 한 단지 탐색 완료
            cnts.append(cnt)                        # 해당 단지의 cnt 값을 cnts에 저장

length = len(cnts)
for i in range(length - 1, 0, -1):                  # 단지 내 집 수 오름차순 정렬 (by 버블)
    for j in range(i):
        if cnts[j] > cnts[j + 1]:
            cnts[j], cnts[j + 1] = cnts[j + 1], cnts[j]

print(length)                                       # 단지 수 출력
for c in cnts:                                      # 각각 단지의 집 수 출력
    print(c)
