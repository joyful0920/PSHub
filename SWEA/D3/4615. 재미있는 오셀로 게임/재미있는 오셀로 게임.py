setting = {4: 1, 6: 2, 8: 3}
stone = ['B', 'W']
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def dfs(x, y):                                  # DFS 함수
    if 0 <= x < n and 0 <= y < n:               # x, y 위치라 범위 내일 때
        if board[x][y] == stone[s - 1]:         # 입력받은 돌과 다른 색 돌이 있다면
            return dfs(x + dx[i], y + dy[i])    # 다른 색 돌이 나올 때까지 재귀 DFS
        elif board[x][y] == stone[s]:           # 같은 색 돌이 나오면
            return True                         # True 반환
    return False                                # 같은 색 돌이 결국 안나오면 False 반환


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    
    # n에 맞게 보드 초기 상태 세팅
    start = setting[n]
    board[start][start], board[start][start + 1] = 'W', 'B'
    board[start + 1][start], board[start + 1][start + 1] = 'B', 'W'

    cnt = [2, 2]                             # 흑백 카운트 변수
    for _ in range(m):
        y, x, s = map(int, input().split())  # y, x, 돌 종류 입력
        y -= 1                               # 인덱스에 맞게 전부 -1
        x -= 1
        s -= 1

        cnt[s] += 1                          # 일단 돌 입력을 받으면
        board[x][y] = stone[s]               # 해당 위치와 돌 갯수 업뎃

        for i in range(8):                            # 그리고 해당 위치 기준 모든 방향에 대해
            nx = x + dx[i]                            # 다음 위치를 세팅하여
            ny = y + dy[i]
            if dfs(nx, ny):                           # DFS 수행 결과가 True => 바꿔 줄 수 있는 돌이 있다!
                while board[nx][ny] == stone[s - 1]:  # 현재 델타 탐색 방향에 위치한 돌들 중
                    board[nx][ny] = stone[s]          # 입력 받은 돌과 다른 색 돌들을
                    cnt[s] += 1                       # 같은 색으로 변경!
                    cnt[s - 1] -= 1
                    nx += dx[i]
                    ny += dy[i]

    print(f'#{tc} {cnt[0]} {cnt[1]}')