# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1=list2=[]
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
