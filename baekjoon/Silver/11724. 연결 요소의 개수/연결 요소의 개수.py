import sys
# sys.stdin = open('input.txt')
si = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(x):                     # DFS by 재귀
    visited[x] = True           # 현 노드 방문 처리함으로써 연결 처리
    for nv in graph[x]:         # 연결된 다른 노드들을 확인하여
        if not visited[nv]:     # 미방문한 노드에 대해
            dfs(nv)             # 재귀 DFS 수행


n, m = map(int, si().split())

graph = [[] for _ in range(n + 1)]      # 그래프 by 인접리스트
for _ in range(m):                      # 엣지 정보를 입력 받아 그래프 완성
    u, v = map(int, si().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = [False] * (n + 1)     # 방문 처리 리스트
for i in range(1, n + 1):       # 모든 노드들에 대해
    if not visited[i]:          # 미방문한 노드들에 대해서만
        cnt += 1                # 연결 요소 개수 + 1 후
        dfs(i)                  # DFS 수행

print(cnt)