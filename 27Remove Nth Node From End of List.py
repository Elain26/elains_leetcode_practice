# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #get the length of the linked list
        p=head
        len1=0
        while p:
            len1+=1
            p=p.next
        index1=len1-n
        #special,if index is 0,remove the first Node
        if index1==0:
            head=head.next
            return head
        #go to the Node, remove the N-th from the end of the list
        p=head
        for i in range(index1):
            if i==index1-1:
                p.next=p.next.next
            p=p.next
            i+=1            
        return head
