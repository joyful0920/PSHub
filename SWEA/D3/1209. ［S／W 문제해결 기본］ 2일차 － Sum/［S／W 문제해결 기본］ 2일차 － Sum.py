for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    for i in range(100):
        # 합 리스트
        sums = [0, 0, 0, 0] # 행 열 대각선왼위오밑 대각선오위왼밑

        for j in range(100):
            sums[0] += arr[i][j]
            sums[1] += arr[j][i]

        sums[2] += arr[i][i] # 대각선: 왼위 -> 오밑
        sums[3] += arr[i][100 - i - 1] # 대각선 오위 -> 왼밑
        
        # 합 중 최댓값 구하기
        for sum in sums:
            if sum > result:
                result = sum


    print(f'#{tc} {result}')