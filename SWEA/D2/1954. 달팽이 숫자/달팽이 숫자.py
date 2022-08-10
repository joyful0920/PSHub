t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, -1
    idx = 0
    num = 0

    loop = n
    while loop >= 0:
        if loop == n:
            for _ in range(loop):
                x += dx[idx]
                y += dy[idx]
                num += 1
                snail[x][y] = num
            idx = (idx + 1) % 4
        else:
            for _ in range(2):
                for _ in range(loop):
                    x += dx[idx]
                    y += dy[idx]
                    num += 1
                    snail[x][y] = num
                idx = (idx + 1) % 4
        loop -= 1

    print(f'#{tc}')
    for i in range(n):
        print(*snail[i])