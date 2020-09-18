#define singly-linked list/Node structure 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#fast goes two step each time and slow goes one step
#when fast reach the end,slow will be at the middle
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #give a start, anyway I am going to change it later
        new_head=None
        #---waiting to modify--head--new_head--finished--
        while head!=None:
            p=head
            head=head.next
            p.next=new_head
            new_head=p
        return new_head
        """
        :type head: ListNode
        :rtype: ListNode
        """
#construct a singly-linked list[1,2,3]
Node1=ListNode(1)
Node2=ListNode(2)
Node3=ListNode(3)
Node4=ListNode(4)
Node5=ListNode(5)
Node1.next=Node2
Node2.next=Node3
Node3.next=Node4
Node4.next=Node5
#check if the middle Node is correct
a=Solution()
ans=a.reverseList(Node1)
print(ans.val,ans.next.val,ans.next.next.val,ans.next.next.next.val,ans.next.next.next.next.val)
