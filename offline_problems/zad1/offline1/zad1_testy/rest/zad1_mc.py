from zad1testy import runtests
'''
Mateusz Cyganek
O (n * k)
Zasada działania podobna jak w insertion sorcie: dla każdego node-a szukam w zasięgu k wartości minimalnej i odpowiednio przepinam node-y
'''
def findHead(p, k, parent):
    curr, minNode = p, p
    currParent, minParent = parent, parent
    i = 0
    while i < k and curr.next:
        currParent = curr
        curr = curr.next
        if curr.val < minNode.val: minNode, minParent = curr, currParent
        i += 1
    if minNode.val < p.val and p.next and p.next.val == minNode.val: # przepinanie z sąsiadem
        memLink1, memLink2 = p.next.next, p
        p.next, minNode.next = memLink1, memLink2
        parent.next = minNode
        return minNode
    elif minNode.val < p.val: # przepinanie odległych node-ów
        memLink1, memLink2 = p.next, minNode.next
        p.next, minNode.next = memLink2, memLink1
        if minParent is not None:
        	parent.next, minParent.next = minNode, p
        return minNode
    else: return p

def SortH(p, k):
    parent = None
    head = findHead(p, k, parent) # zapamiętuje głowę
    while p and p.next:
        parent = p
        p = p.next
        p = findHead(p, k, parent)
    return head

runtests( SortH ) 
