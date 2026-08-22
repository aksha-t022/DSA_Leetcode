# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        H=None
        P=None
        while l1 and l2:
            if l1.val<l2.val:
                temp=l1
                l1=l1.next
                temp.next=None
                if (H==None):
                    H=P=temp
                else:
                    P.next=temp
                    P=temp
            else:
                temp=l2
                l2=l2.next
                temp.next=None
                if (H==None):
                    H=P=temp
                else:
                    P.next=temp
                    P=temp
        while l1:
            temp=l1
            l1=l1.next
            temp.next=None
            if (H==None):
                H=P=temp
            else:
                P.next=temp
                P=temp
        while l2:
            temp=l2
            l2=l2.next
            temp.next=None
            if (H==None):
                H=P=temp
            else:
                P.next=temp
                P=temp
        return H
