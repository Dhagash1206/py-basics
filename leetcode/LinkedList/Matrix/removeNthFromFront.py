def removeNthFromFront(head, n):
    if head is None:
        return None

    if n == 1:
        return head.next

    temp = head

    for i in range(n - 2):
        temp = temp.next

    temp.next = temp.next.next

    return head