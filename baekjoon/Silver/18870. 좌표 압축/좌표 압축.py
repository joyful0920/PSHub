import sys
# sys.stdin = open('input.txt')
si = sys.stdin.readline

n = int(si())
numbers = list(map(int, si().split()))
sorted_numbers = sorted(numbers)    # 입력 받은 숫자 오름차순 정렬

cnts = dict()                       # 카운트 딕셔너리 숫자(key): 자기보다 작은 숫자 종류(value)
for number in sorted_numbers:       # 존재하는 숫자들에 대해서
    cnts[number] = 0                # cnts 값 0으로 초기화

for i in range(1, n):
    if sorted_numbers[i] > sorted_numbers[i - 1]:   # 정렬된 숫자를 하나씩 확인하며
        # 직전 숫자보다 클 경우에만 직전 숫자의 cnts 값 + 1을 지금 숫자의 cnts 값으로!
        cnts[sorted_numbers[i]] += cnts[sorted_numbers[i - 1]] + 1

for number in numbers:
    print(cnts[number], end=' ')
