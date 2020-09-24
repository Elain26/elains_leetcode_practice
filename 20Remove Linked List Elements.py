class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        #给一个空的头
        p0=ListNode(0)
        #这个头接原来的head
        p0.next=head
        #指针指向head
        p1=p0
        #当指针和指针下一个都有的话
        while p1 and p1.next:                      
            if p1.next.val==val:
                p1.next=p1.next.next
            else:
                p1=p1.next
        return p0.next

Node1=ListNode(1)
"""Node2=ListNode(2)
Node3=ListNode(3)
Node4=ListNode(4)
Node1.next=Node2
Node2.next=Node3
Node3.next=Node4"""
a=Solution()
ans=a.removeElements(Node1, 1)
print(ans)
