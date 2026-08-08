class Solution:
    def merge(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        # Merge both sorted lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Add remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

    def sortList(self, head):
        # 0 or 1 node is already sorted
        if not head or not head.next:
            return head

        # Find the middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split into two lists
        second_half = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(second_half)

        # Merge the sorted halves
        return self.merge(left, right)