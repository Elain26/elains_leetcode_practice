
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
