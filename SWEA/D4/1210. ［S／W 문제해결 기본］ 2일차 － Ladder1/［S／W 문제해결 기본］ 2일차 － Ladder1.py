dx = [0, 0, -1]
dy = [-1, 1, 0]

for _ in range(10):
    tc = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    end = [99] + [i for i in range(100) if ladders[99][i] == 2]

    x, y = end[0], end[1]
    while x > 0:
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100 and ladders[nx][ny] == 1:
                ladders[x][y] = 0 # 지나간 사다리는 0으로 처리해서 다시 돌아가지 않도록!
                x, y = nx, ny

    print(f'#{tc} {y}')