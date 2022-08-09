def rotation(array):
    results = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            results[i][j] = array[-j - 1][i]
    return results

t = int(input())

for test in range(1, t + 1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    result = [list([] for _ in range(3)) for _ in range(n)]

    for r in range(3):
        array = rotation(array)
        for i in range(n):
            for j in range(n):
                result[i][r].append(array[i][j])
    
    print(f"#{test}")
    for i in range(n):
        for r in range(3):
            for j in range(n):
                if j == n - 1:
                    if r == 2:
                        print(result[i][r][j])
                    else:
                        print(result[i][r][j], end=' ')    
                else:
                    print(result[i][r][j], end='')