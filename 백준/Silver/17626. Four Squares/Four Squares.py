import sys, math
# sys.stdin = open('input.txt')
si = sys.stdin.readline
INF = float('inf')

n = int(si())

dp = [INF] * (n + 1)    # 정수 표현에 필요한 제곱수의 최소개수 DP 테이블
dp[0], dp[1] = 0, 1     # 정수 0과 1은 각각 0개, 1개로 저장

if n > 1:                                       # 목표 n이 1보다 클 경우
    for i in range(2, n + 1):                   # 차례차레 최소개수를 계산하며 목표값으로!
        num = int(math.sqrt(i))                 # 현재 정수 i보다 같거나 작은 수의 제곱근 중 최대
        while num != 0:                         # num이 0이 아닐 동안
            if 1 + dp[i - num ** 2] < dp[i]:    # 직전 인덱스들의 dp 값을 활용하여
                dp[i] = 1 + dp[i - num ** 2]    # dp[i]의 최소값 갱신
            num -= 1                            # 하나의 테스트가 끝나면 num - 1

print(dp[n])
