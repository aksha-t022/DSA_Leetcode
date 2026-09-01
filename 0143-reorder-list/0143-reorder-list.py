# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        sp = fp = head
        while fp.next and fp.next.next:
            sp = sp.next
            fp = fp.next.next

        temp = sp.next
        sp.next = None

        prev = None
        curr = temp
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        temp = prev

        start = end = head
        head = head.next
        start.next = None

        while head and temp:
            tm = temp
            temp = temp.next
            tm.next = None
            end.next = tm
            end = tm

            tm = head
            head = head.next
            tm.next = None
            end.next = tm
            end = tm

        if temp:
            end.next = temp