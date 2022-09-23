dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, num, depth):               # DFS 함수.
    num += board[x][y]                   # 인자로 받은 숫자에 현재 board 숫자 이어 붙여주기
    if depth == 7:                       # 7자리가 완성됐다면
        results.add(num)                 # 결과 리스트에 저장하고
        return                           # 현재 재귀는 끝

    for i in range(4):                   # 현 x, y 기준
        nx = x + dx[i]                   # 상하좌우 다음 위치 세팅하여
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:  # 범위 내라면
            dfs(nx, ny, num, depth + 1)  # 현재 num과 depth를 활용하여 재귀 DFS


for tc in range(1, int(input()) + 1):
    board = [list(map(str, input().split())) for _ in range(4)]

    results = set()                 # 중복 제거를 위해 results 자료 구조를 셋으로
    for i in range(4):
        for j in range(4):
            dfs(i, j, '', 1)        # 모든 지점에 대해 DFS 수행

    print(f'#{tc} {len(results)}')