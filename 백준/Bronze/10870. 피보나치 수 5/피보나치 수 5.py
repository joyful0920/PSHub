import sys

# sys.stdin = open('input.txt')
si = sys.stdin.readline


# 피보나치 함수 by 재귀
def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


n = int(si())
print(fibonacci(n))
