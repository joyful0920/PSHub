import sys
si = sys.stdin.readline

# 강의 수와 블루레이 개수 입력
n, m = map(int, si().split())

# 강의 길이 입력(순서 대로)
array = list(map(int, si().split()))

def blueray():
    # 이진 탐색을 위한 시작점과 끝점 설정
    start = max(array)
    end = sum(array)

    # 이진 탐색 수행(반복적)
    minsize = 0 # 블루레이 최소 크기 초기화
    while (start <= end):
        mid = (start + end) // 2
        size = mid # 블루레이 현재 크기 초기화
        total = 0 # 각각의 블루레이에 들어가는 강의 전체 길이 초기화
        cnt = 1 # 블루레이 사용 갯수 카운트 변수 초기화

        # 블루레이가 최소 크기를 만족하는지 계산
        for i in range(n):
            total += array[i]
            if total > size:
                cnt += 1
                total = array[i]

        # 소비한 블루레이 개수가 m보다 크면 블루레이 크기를 더 크게
        if cnt > m:
            start = mid + 1
        # 소비한 블루레이 개수가 m보다 같거나 작으면
        else:
            minsize = size
            end = mid - 1

    return minsize

print(blueray())