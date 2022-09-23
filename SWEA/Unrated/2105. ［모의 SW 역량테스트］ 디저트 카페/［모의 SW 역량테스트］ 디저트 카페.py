from heapq import heappush

# 다음 방문 위치를 정할 델타 탐색 2차원 리스트: 모두 대각선 방향
dx = [[1, 1], [1, -1], [-1, -1], [-1, 1]]   # 오른쪽 아래, 왼쪽 아래, 왼쪽 위, 오른쪽 위 순
dy = [[1, -1], [-1, -1], [-1, 1], [1, 1]]   # 각각의 요소 또한 리스트인데,
                                            # 현재 방향을 유지할 것인지 시계방향으로 한번 틀 것인지에 대한 인덱스가 담겨 있음!

def dfs(x, y, visited, cnt, di):                # 행, 열 인덱스, 방문 처리 배열, 디저트 수, 현재 이동 방향 인덱스를 인자로
    if len(visited) == 1 and x == start[0] and y == start[1]:   # 시작점인 경우
        nx = x + dx[di][0]                      # 무조건적으로 오른쪽 아래 방향으로 이동 가능!
        ny = y + dy[di][0]                      # why? 아래 오른쪽 방향으로 이동 가능한 곳에서만 DFS를 돌렸기 때문에!
        if cafe[nx][ny] not in visited:         # 같은 디저트를 팔고 있는지만 확인해서
            visited.append(cafe[nx][ny])        # 중복되지 않는다면 방문 처리 리스트에 해당 디저트 종류를 넣어주고,
            dfs(nx, ny, visited, cnt + 1, di)   # 현재 방향(오른쪽 아래)으로 계속 DFS 수행
        return

    for i in range(2):                                      # 시작점이 아닌 경우, 2번 반복
        nx = x + dx[di][i]                                  # 뭐를? => 다음 이동 좌표 정해서 이동하는 걸!
        ny = y + dy[di][i]                                  # 현재 방향을 유지하는 경우 & 시계방향으로 한번 방향 트는 경우
        if 0 <= nx < n and 0 <= ny < n:                     # 다음 위치가 범위 내라면
            if nx == start[0] and ny == start[1]:           # 시작점으로 돌아온 경우
                heappush(result, (-cnt, cnt))               # 최대 힙에 카운트 값을 넣어주고
                return                                      # 현재 함수는 종료
            if cafe[nx][ny] not in visited:                 # 아직 방문 안한 곳이면?
                visited.append(cafe[nx][ny])                # 방문 처리 해주고,
                if di + i < 4:                              # 방향을 몇번 틀었는지 확인해서, 한 사이클 내인 경우만
                    dfs(nx, ny, visited, cnt + 1, di + i)   # DFS 수행
                visited.pop()                               # 수행 후 직전 방문 내용을 제거해서 백트래킹


for tc in range(1, int(input()) + 1):
    n = int(input())
    cafe = [list(map(int, input().split())) for _ in range(n)]

    result = [(1, -1)]                                  # 결과값 최대 힙. (-디저트 수, 디저트 수) 튜플이 요소로 들어감.
    for i in range(n - 2):                              # DFS 돌릴 건데, 실질적으로 사각형을 만들 수 있는 범위에 대해서만!
        for j in range(1, n - 1):                       # 그림에서 규칙을 찾아 보면, 행 인덱스는 0 ~ n - 1, 열 인덱스는 1 ~ n - 2 범위에서 시작할 때만 사각형을 만들 수 있음!
            start = (i, j, cafe[i][j])                  # 현재 행과 열 인덱스, 디저트 종류를 튜플로 묶어 start로!
            dfs(start[0], start[1], [start[2]], 1, 0)   # visited 배열에 시작 위치 디저트 종류를 집어 넣고, DFS 수행

    print(f'#{tc} {result[0][1]}')                      # 최대 힙이기 때문에 가장 앞 요소에 최대값이 위치하게 됨.
