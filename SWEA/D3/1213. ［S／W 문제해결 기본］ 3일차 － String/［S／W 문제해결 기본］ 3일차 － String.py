for _ in range(10):
    tc = int(input())
    s = input()
    sentence = input()

    cnt = 0
    for i in range(len(sentence) - len(s) + 1): # 완전 탐색
        if sentence[i:i + len(s)] == s:
            cnt += 1

    print(f'#{tc} {cnt}')