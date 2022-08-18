def dfs(v):                                     # DFS 함수
    visited[v] = True                           # 현재 정점 방문 처리

    for w in graph[v]:                          # 방문한 정점의 인접 노드 확인
        if not visited[w]:                      # 방문 가능한 정점이 있다면
            v = w                               # 다음 방문 정점으로
            dfs(v)                              # 재귀적 DFS 수행


for _ in range(10):
    tc, e = map(int, input().split())
    edges = list(map(int, input().split()))     # 간선 정보

    graph = [[] for _ in range(100)]            # 인접 리스트 graph
    visited = [False] * 100                     # visited 리스트
    for i in range(0, 2 * e, 2):                # 간선 정보 리스트를 step 2로 순회
        graph[edges[i]].append(edges[i + 1])    # graph 완성

    dfs(0)

    if visited[99]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')