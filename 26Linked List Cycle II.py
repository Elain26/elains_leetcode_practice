# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #先判断是否循环
        if head is None or head.next is None:
            return 
        slow=fast=head
        if_Cycle=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                if_Cycle=1
                break
        if if_Cycle==0:
            return
        #把slow指针重置到开头
        slow=head
        #两个同速指针相遇时就是循环点啦
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
