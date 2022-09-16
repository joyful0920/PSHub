from collections import deque

dx = [  # 상좌하우순
    [],
    [-1, 0, 1, 0],  # type 1
    [-1, 0, 1, 0],  # type 2
    [0, 0, 0, 0],   # type 3
    [-1, 0, 0, 0],  # type 4
    [0, 0, 1, 0],   # type 5
    [0, 0, 1, 0],   # type 6
    [-1, 0, 0, 0]   # type 7
]

dy = [
    [],
    [0, -1, 0, 1],
    [0, 0, 0, 0],
    [0, -1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, -1, 0, 0],
    [0, -1, 0, 0]
]


def bfs():
    q = deque([(r, c, 1)])                      # 큐에 맨홀 좌표와 걸린 시간 1로 삽입
    visited = [[False] * m for _ in range(n)]   
    visited[r][c] = True                        # 맨홀 위치 방문 처리

    cnt = 0                     # 카운트 변수
    while q:                    # 큐에 원소가 있는 동안
        x, y, t = q.popleft()   # 지도의 x, y 지점과 걸린 시간 pop

        if t <= l:              # 경과된 시간 내에 이동 가능한 장소라면
            cnt += 1            # 카운트 + 1

        s = graph[x][y]         # 구조물 종류를 s에 저장
        for i in range(4):      # 델타 탐색
            nx, ny = x + dx[s][i], y + dy[s][i]     # 구조물에 맞게 다음 위치 지정
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 0:
                                                    # 범위 내 & 미방문 & 구조물인 위치라면
                ns = graph[nx][ny]                  # 다음 위치의 구조물 타입을 ns에 저장
                j = (i + 2) % 4                     # 다음 위치 구조물의 델타 탐색 인덱스
                                                    # 현재 위치와 다음 위치의 구조물이 서로 맞물려야 함!
                if dx[s][i] + dx[ns][j] == 0 and dy[s][i] + dy[ns][j] == 0:
                    visited[nx][ny] = True          # 맞물리는 경우 이동 가능!
                    q.append((nx, ny, t + 1))

    return cnt


for tc in range(1, int(input()) + 1):
    n, m, r, c, l = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{tc} {bfs()}')