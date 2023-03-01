from zad1testy import Node, runtests


def SortH(p,k):
    if k == 0:
        return p
    elif k == 1:
        head = p
        while p.next is not None:
            if p.val > p.next.val:
                p.val, p.next.val = p.next.val, p.val
                p = p.next
                if p.next is None:
                    return p
            p = p.next
        return head
    else:
        head = Node()
        head.next = p
        p = head
        while p is not None and p.next is not None:
            min_p = p
            min_v = p.next.val
            q = p.next
            i = 0
            while q.next is not None and i < k:
                if q.next.val < min_v:
                    min_p = q
                    min_v = q.next.val
                i += 1
                q = q.next
            if p != min_p:
                # p.next, min_p.next.next, min_p.next = min_p.next, p.next, min_p.next.next
                p.next.val, min_p.next.val = min_v, p.next.val

            p = p.next
        return head.next
# end

runtests( SortH )