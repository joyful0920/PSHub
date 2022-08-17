t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    dp = [[1] * (i + 1) for i in range(n)] # DP 테이블 초기화

    # 값 변경이 필요한 DP 테이블의 행과 열에 대해
    for i in range(2, n):
        for j in range(1, i):
            # 직전 행의 왼쪽 위 열과 바로 위 열 요소 더한 값이
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  # 현재 행의 열 값

    print(f'#{tc}')
    for i in range(n):
        print(*dp[i])
