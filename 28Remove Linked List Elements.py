# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if head is None:
            return
        if head.val==val and head.next is None:
            return
        p=ListNode(0)
        p.next=head
        while p and p.next:
            if p.next.val==val:
                p.next=p.next.next
                continue
            p=p.next
        return head
