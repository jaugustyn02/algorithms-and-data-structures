from random import randint


class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None
# end


def printll(p):
    if p is None:
        return
    result = find_cycle(p)
    if not result:
        print(p.value, end=" ")
        p = p.next
        while p is not None:
            print("->", p.value, end=" ")
            p = p.next
        print()
    else:
        cycle_beg, cycle_len = result
        while p is not cycle_beg:
            print(p.value, end=" -> ")
            p = p.next
        print("(", p.value, end=" ")
        p = p.next
        for _ in range(cycle_len-1):
            print("->", p.value, end=" ")
            p = p.next
        print(")")
# end


def gen_rand_ll(a=1, b=100, n=10):
    if n < 1:
        return None
    head = Node(randint(a, b))
    prev = head
    for _ in range(n):
        new_node = Node(randint(a, b))
        prev.next = new_node
        prev = new_node

    return head
# end


def find_cycle_len(head):
    if head is None:
        return 0

    p = head    # slow
    q = head.next   # fast
    while q is not None and q.next is not None and p != q:
        p, q = p.next, q.next.next

    if p != q:     # p != q => q or q.next must be a None => there is no cycle => cycle length = 0
        return 0

    cycle_len = 1
    q = p.next
    while p != q:
        q = q.next
        cycle_len += 1

    return cycle_len
# end


def find_cycle_beg(head=None, cycle_len=0):
    if head is not None and cycle_len > 0:
        p = head
        while True:
            q = p
            for _ in range(cycle_len):
                q = q.next

            if p == q:
                return p

            p = p.next
# end


def find_cycle(head):
    cycle_len = find_cycle_len(head)
    if cycle_len == 0:
        return False
    return find_cycle_beg(head, cycle_len), cycle_len
# end
