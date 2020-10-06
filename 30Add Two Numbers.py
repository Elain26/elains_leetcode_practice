# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #two new string
        num1=''
        num2=''
        #add all the number to the string
        while l1:
            num1+=str(l1.val)
            l1=l1.next
        while l2:
            num2+=str(l2.val)
            l2=l2.next
        #reverse two string and add up, then get the string of sum, then reverse the number of sum
        num3=str(int(num1[::-1])+int(num2[::-1]))[::-1]
        n=len(num3)
        #give a dummy head
        dummy=p=ListNode(0)
        for i in range(n):
            node=ListNode(num3[i])
            p.next=node
            p=p.next
        return dummy.next
#test
node11=ListNode(2)
node12=ListNode(4)
node13=ListNode(3)
node11.next=node12
node12.next=node13

node21=ListNode(5)
node22=ListNode(6)
node23=ListNode(4)
node21.next=node22
node22.next=node23

a=Solution()
head=a.addTwoNumbers(node11,node21)
print(head.val,head.next.val,head.next.next.val)
