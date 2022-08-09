def counting_sort(arr, k):
    count = [0] * (k + 1)
    for i in arr:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    result = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        count[arr[i]] -= 1
        result[count[arr[i]]] = arr[i]

    return result


for tc in range(1, 11):
    n = int(input())
    boxs = list(map(int, input().split()))

    while n > 0:
        boxs = counting_sort(boxs, 100)
        if boxs[0] + 1 == boxs[-1]:
            break

        n -= 1
        boxs[0] += 1
        boxs[-1] -= 1

    boxs= counting_sort(boxs, 100)
    print(f'#{tc} {boxs[-1] - boxs[0]}')