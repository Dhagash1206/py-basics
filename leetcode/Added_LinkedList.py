class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        p1, p2 = l1, l2

        while p1 or p2 or carry:
            s = carry

            if p1:
                s += p1.val
                p1 = p1.next

            if p2:
                s += p2.val
                p2 = p2.next

            carry = s // 10

            cur.next = ListNode(s % 10)
            cur = cur.next

        return dummy.next