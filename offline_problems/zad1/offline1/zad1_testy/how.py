import time


class Node:
    def __init__(self):
        self.val = None
        self.next = None


n = int(input())
p = Node()
q = Node()
k = Node()
p.next = q
q.next = k
k.next = p
begin = time.time()

for i in range(n):
    p.next, q.next, k.next = q.next, p, q
    p = p.next
    q = q.next
    k = k.next

end = time.time()
print("time:", round(end - begin, 2))
