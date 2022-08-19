for tc in range(1, 11):
    m = int(input())
    words = [input() for _ in range(8)]

    result = 0
    for i in range(8):                  # 가로 검사
        for j in range(0, 8 - m + 1):   # j 인덱스 범위는 회문 길이를 고려해서
            word = words[i][j:j + m]
            if word == word[::-1]:
                result += 1

    for j in range(8):                  # 세로 검사
        for i in range(0, 8 - m + 1):   # i 인덱스 범위는 회문 길이를 고려해서
            word = ''
            for k in range(m):
                word += words[i + k][j]
            if word == word[::-1]:
                result += 1

    print(f'#{tc} {result}')
