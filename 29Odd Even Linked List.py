# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #special, if input is None
        if head is None:
            return
        #give odd and even a head
        odd=head
        even=head2=head.next
        #they should move together,generate 2 link list
        while odd.next and even.next:
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        #connect 2 link
        odd.next=head2   
        return head
node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
a=Solution()
a.oddEvenList(node1)
