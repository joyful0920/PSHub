t = int(input())

for test in range(1, t + 1):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if len(a) > len(b):
        result = 0
        for i in range(len(a) - len(b) + 1):
            temp = 0
            for j in range(len(b)):
                temp += a[i + j] * b[j]
            if temp > result:
                result = temp
    else:
        result = 0
        for i in range(len(b) - len(a) + 1):
            temp = 0
            for j in range(len(a)):
                temp += b[i + j] * a[j]
            if temp > result:
                result = temp

    print(f"#{test} ", end='')
    print(result)