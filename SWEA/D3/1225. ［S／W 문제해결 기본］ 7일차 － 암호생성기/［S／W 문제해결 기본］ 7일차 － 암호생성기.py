for _ in range(10):
    tc = int(input())
    numbers = list(map(int, input().split()))

    cycle = [1, 2, 3, 4, 5]                         # 사이클 리스트
    i = 0                                           # 사이클 인덱스
    while numbers[0] > cycle[i]:                    # 숫자 배열의 첫번째 원소가 현재 사이클 값보다 클 경우만
        numbers.append(numbers.pop(0) - cycle[i])   # 첫번째 원소를 pop해 현재 사이클값을 빼주고 다시 append
        i = (i + 1) % 5                             # 사이클 인덱스 +1

    numbers.pop(0)              # 사이클 값이 배열의 첫 번째 원소보다 클 경우엔 그대로 pop 후 
    numbers.append(0)           # 0을 숫자 배열 뒤에 추가

    print(f'#{tc}', end=' ')
    print(*numbers)