#define singly-linked list/Node structure 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#fast goes two step each time and slow goes one step
#when fast reach the end,slow will be at the middle
class Solution(object):
    def middleNode(self, head):
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
#this is for checking the result
        print(slow.val)  
        return slow
        """
        :type head: ListNode
        :rtype: ListNode
        """
#construct a singly-linked list[1,2,3]
Node1=ListNode(1)
Node2=ListNode(2)
Node3=ListNode(3)
Node1.next=Node2
Node2.next=Node3
#check if the middle Node is correct
a=Solution()
ans=a.middleNode(Node1)
print(ans)
