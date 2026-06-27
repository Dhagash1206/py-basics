class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        count = 0
        temp = head
        while temp != None:
            count +=1
            temp = temp.next


        n = count - n 

        if n == 0:
            return head.next

        temp = head
        
        for _ in range(n - 1):
            temp = temp.next

        temp.next = temp.next.next

        return head