# ZAD 2
# Algorytm polega na sposortowaniu listy sortowaniem przypominającym
# sortowanie bąbelkowe. Z tym, że zamiast przebiegać listę n razy
# wystarczy ją przejść k razy, gdyż elementy przesunięte są jedynie o
# maksymalnie k pozycji.
#
# Złożoność czasowa:
# dla k=Θ(1) wynosi O(n)
# dla k=Θ(logn) wynosi O(nlog(n))
# dla k=Θ(n) wynosi O(n^2)
#
# Złożoność pamięciowa: Algorytm wykonywany w miejscu
#
# W celu usprawnienia sortowania jeżeli k >> log(n) można użyć mergesorta.
# Wtedy złożoność dla k=Θ(n) wynosi O(nlog(n))
# Przed przystąpieniem do sortowania można porównać długość listy do K 
# i w ten sposób decysować który algorytm użyć

from zad1testy import runtests


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def list_bubble_sort(p, k):
    for i in range(k):
        c = p
        while p.next != None:
            if p.val > p.next.val:
                p.val, p.next.val = p.next.val, p.val
            p = p.next
        p = c
    return c


# Merge sort na listach
# Scalanie 2 list posortowanych
#
# def merge_sorted_lists(first: Node, second: Node) -> Node:
#     final = None
#     if first.val > second.val:
#         final = second
#         second = second.next
#     else:
#         final = first
#         first = first.next
#     result = final
#     while first != None and second != None:
#         if first.val > second.val:
#             final.next = second
#             second = second.next
#         else:
#             final.next = first
#             first = first.next
#         final = final.next
#
#     if first != None:
#         final.next = first
#     else:
#         final.next = second
#     return result
#
#
# Natural Merge Sort - Sortowanie przez scalanie naturalne
#
# def divide_into_series(first: Node):
#     # Umieszczanie posortowanych serii w tabeli
#     T = []
#     while first != None:
#         T.append(first)
#         prev = first
#         first = first.next
#         while first != None and prev.val <= first.val:
#             prev = first
#             first = first.next
#         prev.next = None
#     return T
#
#
# def recursive_merge(T, l, r):
#     if (r-l) <= 1:
#         return T[l]
#     mid = (l + r)//2
#     recursive_merge(T, l, mid)
#     recursive_merge(T, mid, r)
#     T[l] = (merge_sorted_lists(T[l], T[mid]))
#     return T[l]
#
#
# def natural_mergesort(first):
#     T = divide_into_series(first)
#     return recursive_merge(T, 0, len(T))
#
#
# WYWOŁANIE natural merge sort:
# natural_mergesort(p)


def SortH(p, k):
    return list_bubble_sort(p, k)


runtests(SortH)
