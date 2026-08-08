class Solution:
    def merge(self, a, b):
        dummy = ListNode(0)
        temp = dummy

        # Merge both lists
        while a and b:
            if a.val < b.val:
                temp.next = a
                a = a.next
            else:
                temp.next = b
                b = b.next

            temp = temp.next

        # Add remaining nodes
        if a:
            temp.next = a
        else:
            temp.next = b

        return dummy.next

    def sortList(self, head):
        # 0 or 1 node
        if not head or not head.next:
            return head

        # Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        second = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(second)

        # Merge sorted halves
        return self.merge(left, right)