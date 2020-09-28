# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """ 
        #count the length of linked list A and B
        p,q=headA,headB
        lenA=lenB=0
        while p:
            lenA+=1
            p=p.next
        while q:
            lenB+=1
            q=q.next 
        #remove the longer part, make them link with same length
        if lenA>lenB:
            for i in range(lenA-lenB):
                headA=headA.next
        if lenB>lenA:
            for i in range(lenB-lenA):
                headB=headB.next
        #then started to find the intersection Node
        #if can't find, at the end of the linked list is also none
        while headA!=headB:
            headA=headA.next
            headB=headB.next
        return headA
