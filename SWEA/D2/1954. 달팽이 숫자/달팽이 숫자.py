# 델타 탐색을 위한 방향 인덱스
dx = [0, 1, 0, -1] # 동 남 서 북
dy = [1, 0, -1, 0]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)] # 달팽이 2차원 리스트

    x, y, idx = 0, 0, 0 # 초기값 세팅
    for i in range(1, n ** 2 + 1):
        snail[x][y] = i
        
        # 달팽이가 이동합니다
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        # 다음 인덱스가 범위 내이고, 아직 지나가지 않은 칸이라면 이동
        if 0 <= nx < n and 0 <= ny < n and not snail[nx][ny]:
            x, y = nx, ny
        else:
            # 방향 인덱스는 3을 넘지 않도록 4로 나눈 나머지로 업뎃!
            idx = (idx + 1) % 4
            x += dx[idx]
            y += dy[idx]

    print(f'#{tc}')
    for i in range(n):
        print(*snail[i])