# from random_list import create_dense_list
# import time

from random import randint, seed

seed(42)


def create_random_list(n, a, b):
    return [randint(a, b) for _ in range(n)]
    
    
def create_dense_list(n, a, b, k):
    A = [randint(a+500, a+1000)/randint(2, 8) for _ in range(k)]
    B = [randint(a, b)/1 for _ in range(n-k) ]
    return A + B
    
    
# T = create_dense_list(1000, 1, 1000, 100)
# print(T)


# T = create_dense_list(550000, 1, 550000, 100000)
#
# begin = time.time()
# SortTab(T, T)
# end = time.time()
# print("czas:", round(end-begin, 5))