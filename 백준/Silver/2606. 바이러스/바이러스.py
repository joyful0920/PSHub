import sys

# sys.stdin = open('input.txt')
si = sys.stdin.readline


def dfs(v):                             # DFS by 재귀
    global cnt
    cnt += 1                            # 감염 +1
    visited[v] = True                   # 방문한 컴은 방문 처리

    for w in graph[v]:                  # 현재 컴과 연결된 다른 컴 확인
        if not visited[w]:              # 방문 안한 컴이 있다면
            v = w                       # 다음 방문할 컴 번호 업뎃
            dfs(v)                      # 해당 컴으로 DFS 재귀 수행


n = int(si())
e = int(si())

graph = [[] for _ in range(n + 1)]      # 빈 인접 리스트 for DFS
visited = [False] * (n + 1)             # visited 리스트 for DFS
for _ in range(e):                      # # 간선정보 입력받아 grpah에 등록
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = -1                                # cnt 수는 -1로 초기화(1번 컴 제외)
dfs(1)

print(cnt)