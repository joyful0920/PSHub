def abs(num):
    return num if num >= 0 else -num


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, 11):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for x in range(n):
        for y in range(n):
            for z in range(4):
                nx, ny = x + dx[z], y + dy[z]
                if 0 <= nx < n and 0 <= ny < n:
                    result += abs(nums[x][y] - nums[nx][ny])

    print(f'#{tc} {result}')
