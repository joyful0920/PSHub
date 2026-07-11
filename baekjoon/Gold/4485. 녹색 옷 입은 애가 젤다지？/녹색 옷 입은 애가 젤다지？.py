import sys
from heapq import heappop, heappush
si = sys.stdin.readline
INF = float('inf')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(x, y):                             # 다익스트라 함수
    q = [(cave[x][y], x, y)]                    # 시작점에서 잃는 금액과, 위치를 우선순위 큐에 넣고
    distance = [[INF] * n for _ in range(n)]    # 도둑 맞는 최소 금액 2차원 리스트 생성 
    distance[x][y] = cave[x][y]                 # 시작 위치에서 잃는 금액 세팅

    while q:                                    # 큐에 원소가 있는 동안
        dist, x, y = heappop(q)                 # 큐에서 맨 앞 원소 팝!
        if distance[x][y] < dist:               # 해당 위치에서 지금보다 더 적 금액을 잃는 경우가 이미 존재
            continue                            # 그럼 이번 케이스는 더 이상 볼 필요 X
        for i in range(4):                      # 델타 탐색으로 인접한 다음 위치 세팅
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:     # 동굴 범위 내라면
                nd = cave[nx][ny] + dist        # 다음 위치로 이동했을 때 잃는 금액의 총 합 계산
                if nd < distance[nx][ny]:       # 해당 위치까지 이동했을 때 잃는 최소 금액이라면
                    distance[nx][ny] = nd       # 최소 금액 리스트 업뎃 후
                    heappush(q, (nd, nx, ny))   # 큐에 푸시

    return distance[-1][-1]                     # 최종적으로 n - 1, n - 1 위치에 도착했을 때 잃는 최소 금액 반환


tc = 0
while True:
    n = int(si())
    if not n:       # 0이 나오면
        break       # 프로그램 종료

    tc += 1
    cave = [list(map(int, si().split())) for _ in range(n)]
    print(f'Problem {tc}: {dijkstra(0, 0)}')
