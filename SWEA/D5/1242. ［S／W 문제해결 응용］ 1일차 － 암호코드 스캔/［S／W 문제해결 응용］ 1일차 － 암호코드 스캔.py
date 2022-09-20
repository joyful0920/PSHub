patterns = ['0001101', '0011001', '0010011', '0111101', '0100011',
            '0110001', '0101111', '0111011', '0110111', '0001011']

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = list(set(input().rstrip() for _ in range(n)))

    codes = set()
    for i in range(len(arr)):
        temp = ''
        for j in range(m):
            binary_num = format(int(arr[i][j], 16), 'b')
            length = len(binary_num)
            if length < 4:
                binary_num = '0' * (4 - length) + binary_num
            temp += binary_num

        one = False
        end, cnt = 0, 0
        for j in range(m * 4 - 1, -1, -1):
            if not end and temp[j] == '1':
                one = True
                end = j
                cnt += 1
            elif end:
                if cnt < 32:
                    if one and temp[j] == '0':
                        one = False
                        cnt += 1
                    elif not one and temp[j] == '1':
                        one = True
                        cnt += 1
                else:
                    length = (end - j - 1) // 56 + 1
                    codes.add(temp[end - (56 * length) + 1:end + 1])
                    one = False
                    end, cnt = 0, 0

    result = 0
    for code in list(codes):
        length = len(code)
        thickness = length // 56

        if thickness > 1:
            temp = ''
            for i in range(0, length, thickness):
                temp += code[i]
            code = temp

        temp, total = 0, 0
        for i in range(1, 9):
            breaker = False
            for j in range(10):
                pattern = code[:7]
                if pattern == patterns[j]:
                    if i % 2 == 1:
                        temp += j * 3
                        total += j
                    else:
                        temp += j
                        total += j
                    code = code[7:]
                    breaker = True
                    break
                if breaker:
                    break

        if temp % 10 == 0:
            result += total

    print(f'#{tc} {result}')