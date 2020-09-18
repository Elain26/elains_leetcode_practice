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
        temp=head.next
        
        head.next=None
        temp2=temp.next
        head=temp
        print(head.val,temp2.val)
        while temp2.next!=None:
            temp=temp2.next
            temp2.next=head
            head=temp2
            temp2=temp
            #print(head.val,temp2.val)
        temp2.next=head
        head=temp2

        return head
        """temp=temp2.next
        temp2.next=head
        head=temp2
        temp2=temp
        print(head.val,temp2.val)"""
        
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
print(ans.val,ans.next.val)
