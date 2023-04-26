import sys
input=sys.stdin.readline
def next(arr):
    k = -1
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            k = i
    if k == -1:
        return False
    for i in range(len(arr) - 1, -1, -1):
        if arr[k] < arr[i]:
            m = i
            break
    arr[k], arr[m] = arr[m], arr[k]
    T = arr[:k + 1]
    T.extend(list(reversed(arr[k + 1:])))
    return T


s = int(input())
for _ in range(s):
    n = input().rstrip()
    ans = next(list(n))
    if ans:
        print(''.join(ans))
    else:
        print(n)