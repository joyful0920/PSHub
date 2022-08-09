t = int(input())

for test in range(1, t + 1):
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            temp = 0
            for x in range(m):
                for y in range(m):
                    temp += array[i + x][j + y]
            if temp > result:
                result = temp
    
    print(f'#{test} ', end='')
    print(result)