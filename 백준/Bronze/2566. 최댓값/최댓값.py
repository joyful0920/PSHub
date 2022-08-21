import sys

# sys.stdin = open('input.txt')
si = sys.stdin.readline

nums = [list(map(int, si().split())) for _ in range(9)]

result, mx, my = 0, 0, 0
for i in range(9):
    for j in range(9):
        if nums[i][j] >= result:
            result = nums[i][j]
            mx, my = i + 1, j + 1

print(result)
print(mx, my)
