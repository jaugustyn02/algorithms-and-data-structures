def leftmost_bs(p, r, val, arr):
    while p < r:
        mid = (p + r) // 2
        if val > arr[mid]:
            p = mid + 1
        else:
            r = mid
    return r
# end


def rightmost_bs(l, r, val, arr):
    while l < r:
        mid = (l + r) // 2
        if val < arr[mid]:
            r = mid
        else:
            l = mid + 1
    if arr[r] > val and r > 0: return r-1
    return r
# end


T = [2, 5, 10, 13, 13, 15, 16, 18, 19, 20, 20, 20, 25]
# T = [0, 5, 5, 5]

n = len(T)
x = 1
while x != 0:
	x = int(input("x:"))
	print(leftmost_bs(0, n-1, x, T))
	print(rightmost_bs(0, n-1, x, T))
