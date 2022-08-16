def palindrome(words):
    for m in range(100, 0, -1):
        for i in range(100):
            for j in range(100 - m + 1):
                word = ''
                for k in range(j, j + m):
                    word += words[i][k]
                if word == word[::-1]:
                    return len(word)
        for j in range(100):
            for i in range(100 - m + 1):
                word = ''
                for k in range(i, i + m):
                    word += words[k][j]
                if word == word[::-1]:
                    return len(word)


for _ in range(10):
    tc = int(input())
    arr = [list(map(str, input())) for _ in range(100)]

    print(f'#{tc} {palindrome(arr)}')