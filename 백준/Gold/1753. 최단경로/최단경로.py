import heapq
import sys
si = sys.stdin.readline
INF = int(1e9)

# 노드 개수와 간선 개수 입력
n, m = map(int, si().split())
# 시작 노드 입력
start = int(si())

# 2차원 리스트 생성 및 무한으로 초기화
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

# 노드와 간선 간의 정보 입력
for _ in range(m):
    x, y, z = map(int, si().split())
    graph[x].append((y, z))

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
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

# 다익스트라 알고리즘 수행
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])