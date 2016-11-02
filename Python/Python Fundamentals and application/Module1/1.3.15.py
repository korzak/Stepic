def qwerty(n,k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return qwerty(n - 1, k) + qwerty(n - 1, k - 1)


n, k = map(int, input().split())

print(qwerty(n,k))