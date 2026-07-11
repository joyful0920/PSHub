import sys
from heapq import heappush, heappop
# sys.stdin = open('input.txt')
si = sys.stdin.readline

for _ in range(int(si())):
    k = int(si())
    visited = [False] * k                   # 유효 처리 리스트

    min_heap, max_heap = [], []             # 최소 힙, 최대 힙
    for i in range(k):
        command = si().split()
        num = int(command[1])
        if command[0] == 'I':               # 삽입 커맨드라면
            visited[i] = True               # 해당 인덱스의 숫자 유효 처리
            heappush(min_heap, (num, i))    # 최소 힙에 숫자와 인덱스 삽입
            heappush(max_heap, (-num, i))   # 최대 힙에 숫자와 인덱스 삽입
        else:
            if num == -1:                               # 최솟값 삭제 커맨드라면
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)                   # 최소 힙에서 유효하지 않은 숫자는 모두 팝
                if min_heap:                            # 아직 힙에 원소가 있다면
                    visited[min_heap[0][1]] = False     # 최솟값 해당 숫자 무효 처리
                    heappop(min_heap)                   # 최소 힙에서 팝
            else:                                       # 최대값 삭제 커맨드라면
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)                   # 최대 힙에서 유효하지 않은 숫자는 모두 팝
                if max_heap:                            # 아직 힙에 원소가 있다면
                    visited[max_heap[0][1]] = False     # 최대값 해당 숫자 무효 처리
                    heappop(max_heap)                   # 최대 힙에서 팝

        while min_heap and not visited[min_heap[0][1]]:     # 남아 있는 무효한 숫자 모두 팝 처리
            heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heappop(max_heap)

    if min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
