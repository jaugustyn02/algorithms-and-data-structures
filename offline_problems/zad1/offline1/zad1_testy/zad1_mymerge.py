from zad1testy import Node, runtests


def merge(head1, head2):
    sentinel = Node()
    tmp = sentinel

    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            tmp.next = head1
            head1 = head1.next
        else:
            tmp.next = head2
            head2 = head2.next
        tmp = tmp.next

    while head1 is not None:
        tmp.next = head1
        head1 = head1.next
        tmp = tmp.next

    while head2 is not None:
        tmp.next = head2
        head2 = head2.next
        tmp = tmp.next

    return sentinel.next, tmp
# end


def find_mid(head):
    p = head
    q = head.next
    while q is not None and q.next is not None:
        p = p.next
        q = q.next.next
    return p
# end


def merge_sort(head1):
    if head1.next is None:
        return head1, head1

    mid = find_mid(head1)
    head2 = mid.next
    mid.next = None

    new_head1, _ = merge_sort(head1)
    new_head2, _ = merge_sort(head2)
    return merge(new_head1, new_head2)
# end


def find_k(p, k):
    i = 0
    while p.next is not None and i < k:
        p = p.next
        i += 1
    return p
# end


def k_merge_sort(p, k):
    tail2 = find_k(p, 2 * k - 1)
    head2 = tail2.next
    tail3 = find_k(tail2, k)
    head3 = tail3.next

    tail2.next = None
    main_head, tail2 = merge_sort(p)

    tail1 = find_k(main_head, k - 1)
    while head3 is not None:
        tail3.next = None
        head2, tail3 = merge_sort(head2)

        tail1.next, tail3 = merge(tail1.next, head2)

        tail1, head2, tail3 = find_k(tail1, k), head3, find_k(head3, k - 1)
        head3 = tail3.next

    if head2 is not None:
        head2, _ = merge_sort(head2)
        tail1.next, _ = merge(tail1.next, head2)
    return main_head
# end


def SortH(p, k):
    if k == 0:
        return p
    else:
        return k_merge_sort(p, k)
# end


runtests( SortH )
