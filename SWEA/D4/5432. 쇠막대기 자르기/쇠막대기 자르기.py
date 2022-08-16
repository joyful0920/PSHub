t = int(input())
for tc in range(1, t + 1):
    irons = input().replace('()', '.')

    result = 0
    left, cnt = 0, 0
    for i in irons:
        if i == '(':
            left += 1
        elif i == ')':
            left -= 1
            result += 1
        else:
            result += left

    print(f'#{tc} {result}')