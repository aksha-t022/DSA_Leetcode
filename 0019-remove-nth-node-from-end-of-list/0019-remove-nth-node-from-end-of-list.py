class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = head
        count = 0

        while t:
            count += 1
            t = t.next

        if count == n:
            return head.next

        t = head
        for i in range(count - n - 1):
            t = t.next

        t.next = t.next.next

        return head