from zad1testy import Node, runtests


def create_llist(elements):
    head = Node()
    head.val = elements[0]
    prev = head
    for i in range(1, len(elements)):
        new = Node()
        new.val = elements[i]
        prev.next = new
        prev = new
    return head
# end


def print_llist(head):
    tmp = head
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()
# end


# new_head = create_llist((3, 2, 1, 6, 5, 4, 10, 7))
# print_llist(new_head)


def len_of_llist(p):
    count = 0
    while p:
        p = p.next
        count += 1
    return count
# end


# Function to merge sort
def mergeSort(head):
    if (head.next == None):
        return head
     
    mid = findMid(head)
    head2 = mid.next
    mid.next = None
    newHead1 = mergeSort(head)
    newHead2 = mergeSort(head2)
    finalHead = merge(newHead1, newHead2)
    return finalHead
 
# Function to merge two linked lists
def merge(head1, head2):
    merged = Node()
     
    temp = merged
    # While head1 is not null and head2
    # is not null
    while (head1 != None and head2 != None):
        if (head1.val < head2.val):
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        temp = temp.next
     
    # While head1 is not null
    while (head1 != None):
        temp.next = head1
        head1 = head1.next
        temp = temp.next
     
    # While head2 is not null
    while (head2 != None):
        temp.next = head2
        head2 = head2.next
        temp = temp.next
     
    return merged.next


# Find mid using The Tortoise and The Hare approach
def findMid(head):
    slow = head
    fast = head.next
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow


def SortH(p, k):
    return mergeSort(p)
# end

runtests( SortH )
