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
        #special,if head is None,return NULL
        if head is None:
            return
        #special, if head equal to value,keep iterate head until it starts with a number that is not val
        while head.val==val:
            #and if removes all number that equals to val and there left nothing, return Null
            if head.val==val and head.next is None:
                return
            head=head.next
        #start to remove the number that equals to value
        p=head
        while p and p.next:
            if p.next.val==val:
                p.next=p.next.next
                continue
            p=p.next
        return head
