class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        count = 1

        if head.next == None and n == 1:
            return None

        while p2.next is not None:
            p2 = p2.next
            count = count + 1

        if n == count:   # fix: head removal
            return head.next

        for i in range(count - n - 1):
            p1 = p1.next

        p1.next = p1.next.next
        return head
