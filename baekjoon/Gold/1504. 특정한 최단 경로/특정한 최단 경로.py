import heapq
import sys
si = sys.stdin.readline
INF = int(1e9)

# 정점 개수 및 간선 개수 입력
n, e = map(int, si().split())
start = 1

# 2차원 리스트 생성
graph = [[] for _ in range(n + 1)]

# 정점과 간선 간의 정보 입력
for _ in range(e):
    a, b, c = map(int, si().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 중간점 정보 입력
v1, v2 = map(int, si().split())

# 다익스트라 알고리즘
def dijkstra(start, fin):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[fin]


result = min(dijkstra(start, v1) + dijkstra(v1, v2) + dijkstra(v2, n), dijkstra(start, v2) + dijkstra(v2, v1) + dijkstra(v1, n))
if result >= INF:
    print(-1)
else:
    print(result)