# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #exception, head is empty of head.next is empty
        if head is None or head.next is None:
            return False
        #give pointer slow and fast,slow walks 1 step, fast walks 2 steps
        #if there's a circle, they are going to meet somewhere
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
