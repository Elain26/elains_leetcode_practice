class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
      #新建空列表
        list1=[]
      #搞个指针记一下头
        p=head
      #把链表里的值都记录进列表里
        while head:
            list1.append(head.val)
            head=head.next
        print(list1)
       #把列表里最后一个数和链表里第一个数开始一个一个比对
        l=int(len(list1)/2)
        for i in range(l):
            a=list1.pop()
            if a==p.val:
                p=p.next
            else:
                return False
        return True
        
Node1=ListNode(1)
Node2=ListNode(2)
Node3=ListNode(2)
Node4=ListNode(1)
Node1.next=Node2
Node2.next=Node3
Node3.next=Node4
a=Solution()
ans=a.isPalindrome(Node1)
print(ans)
