t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    submit = list(map(int, input().split()))                        # 제출한 사람 목록

    not_submit = [i for i in range(1, n + 1) if i not in submit]    # 제출하지 않은 사람 목록

    print(f'#{tc}', end=' ')
    print(*not_submit)
