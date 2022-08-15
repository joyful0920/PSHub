t = int(input())
for tc in range(1, t + 1):
    a, b = input().split()
    result = a.replace(b, ' ')

    print(f'#{tc} {len(result)}')