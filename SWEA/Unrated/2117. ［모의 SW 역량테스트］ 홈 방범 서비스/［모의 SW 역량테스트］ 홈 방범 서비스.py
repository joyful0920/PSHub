from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, depth):                           # 마름모 범위를 탐색해줄 DFS
    q = deque([(x, y, depth)])                  # 큐에 시작 위치와 탐색 깊이를 넣어 주고

    visited = [[False] * n for _ in range(n)]   # 방문 처리 리스트
    visited[x][y] = True                        # 시작 지점 방문 처리

    cnt = 0                 # 집 개수 카운트 변수
    if house[x][y] == 1:    # 시작 지점에 집이 있다면
        cnt += 1            # cnt + 1

    while q:                                        # 큐에 요소가 존재하는 동안
        x, y, depth = q.popleft()                   # 팝!
        if depth < k:                               # 탐색 깊이가 k 보다 작다? 아직 마름모 범위 더 탐색 가능
            for i in range(4):
                nx = x + dx[i]                      # 다음 이동 위치 구해서
                ny = y + dy[i]                      # 이동 가능하다면
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:  
                    visited[nx][ny] = True          # 방문 처리
                    if house[nx][ny] == 1:          # 집이 있는 곳이라면
                        cnt += 1                    # 집 개수 카운트 + 1
                    q.append((nx, ny, depth + 1))   # 현 위치와 탐색 깊이를 큐에 삽입

    return cnt


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    house = [list(map(int, input().split())) for _ in range(n)]
    price = [k ** 2 + (k - 1) ** 2 for k in range(n + 2)]   # 필요한 만큼 K 범위를 잡아 운영 비용을 계산해 리스트에 넣어 활용
                                                            # 마름모가 도시를 전부 뒤덮는 경우까지 테스트 해볼려면 n + 1 정도까지 K 범위 필요
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(1, n + 2):               # 모든 K에 대해 테스트
                if k == 1 and house[i][j] == 1:     # K가 1이고 도시가 현 위치에 있다면
                    cnt = 1                         # 당연히 cnt는 1
                else:                               # K가 2부터는
                    cnt = bfs(i, j, 1)              # BFS를 수행하여 마름모 범위 탐색하고 포함되는 집 개수 반환

                margin = cnt * m - price[k]         # 이익을 계산해서
                if margin >= 0 and cnt > result:    # 손해를 안보고, 현재까지 구했었던 result 값보다 크다면
                    result = cnt                    # 최대 집 개수 변수 갱신

    print(f'#{tc} {result}')