# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            if head.val==head.next.val:
                return True
            else:
                return False
        list1=[]
        fast=slow=head
        while fast.next:
            list1.append(slow.val)
            fast=fast.next.next           
            slow=slow.next
            
        while slow:            
            value=list1.pop()
            slow=slow.next
            if slow.val!=value:
                return False
            
        return True
