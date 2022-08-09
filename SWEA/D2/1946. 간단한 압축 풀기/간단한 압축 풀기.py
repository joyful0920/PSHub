t = int(input())

for i in range(1, t + 1):
    n = int(input())
    result = []

    for _ in range(n):
        Ci, Ki = map(str, input().split())
        for _ in range(int(Ki)):
            result.append(Ci)
    
    print(f'#{i}')
    for i in range(len(result)):
        if i % 10 == 9:
            print(result[i])
        else:
            print(result[i], end='')
    print()