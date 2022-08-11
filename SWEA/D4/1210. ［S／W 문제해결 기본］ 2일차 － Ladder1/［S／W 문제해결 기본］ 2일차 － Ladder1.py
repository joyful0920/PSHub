dx = [0, 0, 1]
dy = [-1, 1, 0]

for _ in range(1, 11):
    tc = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    starts = [i for i in range(100) if ladders[0][i]]

    for sy in starts:
        x, y = 0, sy
        toggle = True
        yd = 0
        while x < 99:
            if toggle:
                for i in range(2):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < 100 and 0 <= ny < 100 and ladders[nx][ny]:
                        x = nx
                        y = ny
                        yd = dy[i]
                        toggle = not toggle
                        break
                if toggle:
                    x += 1
            else:
                for i in range(2, 3):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < 100 and 0 <= ny < 100 and ladders[nx][ny]:
                        x = nx
                        y = ny
                        toggle = not toggle
                        break
                if not toggle:
                    y += yd

            if ladders[x][y] == 2:
                print(f'#{tc} {sy}')
                break