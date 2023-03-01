# Złożoność czasowa: O(nlogn)

from queue import PriorityQueue
from collections import deque


class CharNode:
    def __init__(self, i=None):
        self.char_ind = i
        self.left = None
        self.right = None
        self.code = ""
# end


def huffman(S, F):
    n = len(S)
    pqueue = PriorityQueue()
    for i in range(n):
        new_item = F[i], CharNode(i)
        pqueue.put(new_item)
    while pqueue.qsize() > 1:
        item1 = pqueue.get()
        item2 = pqueue.get()
        new_item = item1[0] + item2[0], CharNode()
        new_item[1].left = item1[1]
        new_item[1].right = item2[1]
        pqueue.put(new_item)

    queue = deque()
    queue.append(pqueue.get()[1])
    C = ["" for _ in range(n)]
    C[0] = "1"  # if n == 1
    while len(queue) > 0:
        node = queue.popleft()
        if node.char_ind is not None:
            C[node.char_ind] = node.code
        else:
            node.left.code = node.code + "1"
            node.right.code = node.code + "0"
            queue.append(node.left)
            queue.append(node.right)

    for i in range(n):
        print(S[i], ":", C[i])
    return sum([F[i] * len(C[i]) for i in range(n)])
# end


if __name__ == "__main__":
    S = ["a", "b", "c", "d", "e", "f"]
    F = [10, 11, 7, 13, 1, 20]
    # S = ["a", "x"]
    # F = [10, 50]
    print("dlugosc napisu:", huffman(S, F))
