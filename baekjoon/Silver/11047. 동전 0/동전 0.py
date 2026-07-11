import sys
si = sys.stdin.readline

n, k = map(int, si().split())
coin = [int(si()) for _ in range(n)]
coin.sort(reverse= True)

cnt = 0

for i in range(n):
    if k == 0:
        break
    elif coin[i] <= k:
        cnt += k // coin[i]
        k %= coin[i]

print(cnt)