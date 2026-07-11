import sys
from heapq import heappush, heappop
si = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):                    # 다익스트라 함수
    q = [(0, start)]                    # 우선순위 큐에 시작점 거리와 시작점 넣고
    distance[start] = 0                 # 시작점 최단 거리도 0으로 넣고 시작!

    while q:                            # 큐에 원소가 있는 동안
        dist, now = heappop(q)          # 맨 앞 원소를 팝
        if distance[now] < dist:        # 현재 노드의 최단 거리가 현 dist 보다 작을 떈
            continue                    # 더 이상 볼 필요 X
        for nv, nd in graph[now]:       # 현재 노드와 연결되어 있는 다른 노드 확인
            nd += dist                  # 현재 노드를 거쳐 다음 노드까지의 거리를 계산해서 
            if nd < distance[nv]:       # 해당 노드의 최단 거리라면
                distance[nv] = nd       # 최단 거리 업뎃!
                heappush(q, (nd, nv))   # 그리고 해당 노드와 최단 거리 정보를 큐에 푸시!


v, e = map(int, si().split())           # 노드, 엣지 수
start = int(si())                       # 시작 노드

graph = [[] for _ in range(v + 1)]      # 그래프 by 인접 리스트
for _ in range(e):                      # 그래프에 엣지 정보 입력
    a, b, c = map(int, si().split())    # a -> b로의 거리가 c
    graph[a].append((b, c))

distance = [INF] * (v + 1)      # 최단 거리 리스트 일단 무한으로 즐겨요
dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
