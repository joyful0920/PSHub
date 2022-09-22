from itertools import combinations
from heapq import heappush


def change(arr, depth):                 # 카드 교환 함수
    if depth == n:                      # 주어진 횟수만큼 교환했다면
        num = int(''.join(arr))         # 문자 배열을 이어 붙이고 숫자로 변환
        heappush(results, (-num, num))  # 숫자의 음수 값을 튜플로 묶어 줘서 힙 푸시!
                                        # => 결과적으로 가장 큰 숫자가 맨 앞 요소로 가게 됨.
        return
    
    for case in combinations(list(range(len(number))), 2):           # 교환 가능한 카드 조합 케이스들은 구해서
        temp = arr[:]                                                # 얕은 복사로 카피 떠주고
        temp[case[0]], temp[case[1]] = temp[case[1]], temp[case[0]]  # 카드 교환

        num = int(''.join(temp))        # 현재까지의 횟수(depth)만큼 교환해서 만든 숫자
        if num not in visited[depth]:   # 한번도 만들어본 숫자가 아닌 경우만!
                                        # why? 이미 만든 적 있는 녀석으로 또 재귀 돌리면 너무 비효율적이야~
            visited[depth].append(num)  # 방문 처리 리스트에 넣어주고
            change(temp, depth + 1)     # depth를 1 증가시켜 재귀적으로 change 함수 실행


for tc in range(1, int(input()) + 1):
    number, n = map(str, input().split())
    n = int(n)
    numbers = list(map(str, number))

    results = []                        # 만들 수 있는 금액들을 담을 리스트 -> 최대 힙으로 쓸 거임미다
    visited = [[] for _ in range(n)]    # 방문 처리 리스트

    change(numbers, 0)
    print(f'#{tc} {results[0][1]}')