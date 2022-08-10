for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    # 행
    for i in range(100):
        sum_num = 0
        for j in range(100):
            sum_num += arr[i][j]
        if sum_num > result:
            result = sum_num

    # 열
    for j in range(100):
        sum_num = 0
        for i in range(100):
            sum_num += arr[i][j]
        if sum_num > result:
            result = sum_num

    # 대각선 왼위 -> 오밑
    j = -1
    sum_num = 0
    for i in range(100):
        j += 1
        sum_num += arr[i][j]
    if sum_num > result:
        result = sum_num

    # 대각선 외위 -> 왼밑
    j = 100
    sum_num = 0
    for i in range(100):
        j -= 1
        sum_num += arr[i][j]
    if sum_num > result:
        result = sum_num

    print(f'#{tc} {result}')