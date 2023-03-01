from queue import PriorityQueue


def ksuma( T, k ):
    for i in range(k):
        T[i] = (T[i], i)
    pqueue = PriorityQueue(T[:k])
    for i in range()