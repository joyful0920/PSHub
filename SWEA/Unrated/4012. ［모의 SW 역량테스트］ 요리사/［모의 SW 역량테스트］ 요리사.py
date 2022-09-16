from itertools import combinations

def synergy(half):
    total = 0
    for each in list(combinations(half, 2)):
        total += s[each[0]][each[1]]
        total += s[each[1]][each[0]]

    return total


for tc in range(1, int(input()) + 1):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]

    result = float('inf')                           # 결과 변수를 무한으로 초기화
    foods = list(range(n))                          # 전체 식재료 리스트
    for a in list(combinations(foods, n // 2)):     # a 식재료 조합 구하기
        b = set(foods) - set(a)                     # 차집합으로 b 식재료 조합 구하기

        taste_a = synergy(a)                        # a 맛 구하고
        taste_b = synergy(b)                        # b 맛도 구하고

        temp = abs(taste_a - taste_b)               # 서로 빼주고!
        if temp < result:                           # 결과값보다 작다면
            result = temp                           # result 갱신!

    print(f'#{tc} {result}')