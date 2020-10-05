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
        
        list1=[]
        list2=[]
        while l1:
            list1.append(l1.val)
            l1=l1.next

        while l2:
            list2.append(l2.val)
            l2=l2.next

        number1=0
        number3=1
        for i in range(len(list1)):            
            number1=list1[i]*number3+number1
            number3=10*number3
        #print(number1)
        number2=0
        number3=1
        for i in range(len(list2)):            
            number2=list2[i]*number3+number2
            number3=10*number3

        number4=int(number1+number2)

        length=(len(str(number4)))
        number3=1
        p=dummy=ListNode(0)
        for i in range(length):
            position=int(number4/number3%10)

            node=ListNode(position)
            dummy.next=node
            #print(head.val)
            number3=number3*10
            dummy=dummy.next
        return p.next
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
