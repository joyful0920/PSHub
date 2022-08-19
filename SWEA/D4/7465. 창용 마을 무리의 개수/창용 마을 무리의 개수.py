def dfs(x):                 # DFS 함수
    visited[x] = True       # 방문 처리
    for nx in graph[x]:     # 인접 리스트를 통해 연결된 사람 확인
        if not visited[nx]: # 그 중아직 체크 안한 사람이 있다면
            dfs(nx)         # 재귀 DFS


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]          # 인접 리스트 graph
    visited = [False] * n                   # visited 리스트

    for _ in range(m):                      # 간선 정보 입력
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    cnt = 0
    for i in range(n):                      # 모든 사람에 대해
        if graph[i] and not visited[i]:     # 아는 사람이 있고, 아직 체크하지 않은 사람이라면
            dfs(i)                          # DFS 수행
            cnt += 1                        # 무리 수 + 1

    for g in graph:     # 반례 처리
        if not g:       # 아싸인 경우도
            cnt += 1    # 무리 수 += 1

    print(f'#{tc} {cnt}')