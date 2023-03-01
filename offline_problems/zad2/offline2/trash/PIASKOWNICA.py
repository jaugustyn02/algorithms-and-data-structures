def binary_search(x, l, r, T):
    while l < r:
        m = (l+r)//2
        if x > T[m]:
            l = m+1
        else:
            r = m
    return l


t = [2, 2, 2, 4, 5, 6]
print(t)
l, r = 0, len(t)
while True:
    # l = int(input())
    if l < 0: break
    # r = int(input())

    x = int(input())
    print(binary_search(x, l, r, t))
