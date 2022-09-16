def binary_search(target, start, end):                  # 이진 탐색 함수
    if start > end:                                     # 시작 지점 > 끝 지점 => 목표에 해당하는 값이 없다!
        return -1                                       # 리턴 -1

    mid = (start + end) // 2                            # 중간값 계산
    if mid ** 3 < target:                               # 중간값이 목표값보다 작다면
        return binary_search(target, mid + 1, end)      # 중간값 +1 을 시작 지점으로 재설정해 재귀적으로 이진 탐색!
    if mid ** 3 > target:                               # 중간값이 목표값보다 크다면
        return binary_search(target, start, mid - 1)    # 중간값 -1 을 끝 지점으로 재설정해 재귀적으로 이진 탐색!

    return mid                                          # 위 구문에서 리턴이 없다면 목표값을 찾았다는 것!


for tc in range(1, int(input()) + 1):
    print(f'#{tc} {binary_search(int(input()), 1, 10 ** 18)}')