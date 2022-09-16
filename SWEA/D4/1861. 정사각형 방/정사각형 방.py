from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):                  # BFS 함수
    q = deque([(x, y, 1)])

    while q:                    # 큐에 원소가 존재하는 동안 반복
        x, y, d = q.popleft()   # x, y 인덱스와 현재 이동 횟수 뽑아서
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]   # 그 다음 인덱스 지정하여
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] + 1:
                q.append((nx, ny, d + 1))   # 이동 가능한 경우만 이동 횟수 +1 하여 큐에 삽입

    return d    # 최종적으로 최대 이동 길이 리턴


for tc in range(1, int(input()) + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    result = 0      # 결과 방 번호를 저장할 result 변수
    max_depth = 0   # 최대 이동 횟수
    for i in range(n):
        for j in range(n):
            depth = bfs(i, j)           # 모든 방에 대해 bfs 수행
            if depth == max_depth and graph[i][j] < result:
                result = graph[i][j]    # 이동 횟수는 같지만 방 번호가 더 작은 경우 방 번호 업뎃
            if depth > max_depth:       # 최대 이동 횟수 업뎃
                max_depth = depth
                result = graph[i][j]

    print(f'#{tc} {result} {max_depth}')
