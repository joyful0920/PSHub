from itertools import combinations

for tc in range(1, int(input()) + 1):
    n, b = map(int, input().split())                    
    heights = sorted(list(map(int, input().split())))

    result = sum(heights)                       # 결과값을 모든 점원 키 합으로 초기화
    for i in range(1, len(heights) + 1):        # 모든 점원 수에 대해
        for each in combinations(heights, i):   # 가능한 모든 조합을 구해 보고
            total = sum(each)                   # 해당 경우의 점원 키의 합을 구해서
            if b <= total < result:             # 선반 높이보다 같거나 크고 결과값보다 작은 경우
                result = total                  # 결과값 갱신

    print(f'#{tc} {result - b}')