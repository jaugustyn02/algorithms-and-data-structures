from linked_list_lib import *


def reverse_llist(head):
    p, q = None, head
    while q is not None:
        q.next, q, p = p, q.next, q
    return p
# end


# new_head = gen_rand_ll()
# p = new_head
# while p.next is not None:
#     p = p.next
# p.next = new_head
# printll(new_head)
# new_head = reverse_llist(new_head)
# printll(new_head)

