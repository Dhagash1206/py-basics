class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        p1 = head
        p2 = head.next

        while p1 and p2:
            # swap values
            p1.val, p2.val = p2.val, p1.val

            # move pointers safely
            if p2.next and p2.next.next:
                p1 = p2.next
                p2 = p2.next.next
            else:
                break

        return head