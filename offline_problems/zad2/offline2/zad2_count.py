from zad2testy import runtests


def partition_l(arr, low, high):
    i = low - 1
    pivot = arr[low]

    for j in range(low, high):
        if arr[j][0] < pivot[0] or arr[j][0] == pivot[0] and arr[j][1] > pivot[1]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort_l(arr, low, high):
    if low < high:
        pivot = partition_l(arr, low, high)
        quickSort_l(arr, low, pivot - 1)
        quickSort_l(arr, pivot + 1, high)
        
        
def partition_r(arr, low, high):
    i = low - 1
    pivot = arr[high][1]

    for j in range(low, high):
        if arr[j][1] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort_r(arr, low, high):
    if low < high:
        pivot = partition_r(arr, low, high)
        quickSort_r(arr, low, pivot - 1)
        quickSort_r(arr, pivot + 1, high)


def depth(L):
    n = len(L)
    max_value = 0
    
    for x in L:
        if x[1] > max_value:
            max_value = x[1]
    
    if max_value <= 10**7:
    
            quickSort_l(L, 0, n-1)
            
            T = [0 for _ in range(max_value)]
            
            for x in L:
                T[x[1]-1] += 1
                
            for i in range(max_value-1):
                T[i+1] += T[i]
              
            max_right = 0
            max_counter = 0
            for i in range(n-1):
                r = L[i][1]
                if r > max_right:
                    max_counter = max(max_counter, T[r-1] - i - 1)
                    max_right = r

            return max_counter
            
    else:
        quickSort_r(L, 0, n-1)
        curr_max = L[0][1]
        curr_index = 0
        T = [0 for _ in range(n)]
        for i in range(n):
            if L[i][1] > curr_max:
                curr_max = L[i][1]
                curr_index += 1
                T[curr_index] = T[curr_index-1]
            L[i][1] = curr_index
            T[curr_index] += 1
            
        quickSort_l(L, 0, n-1)
        
        max_right = 0
        max_counter = 0
        for i in range(n-1):
            r = L[i][1]
            if r > max_right:
                max_counter = max(max_counter, T[r-1] - i - 1)
                max_right = r

        return max_counter
        
        return "lepiej nie sprawdzać"



runtests(depth)
