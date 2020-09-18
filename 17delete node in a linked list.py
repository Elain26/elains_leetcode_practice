class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ##value to the next, link to the next
        node.val=node.next.val
        node.next=node.next.next
        
