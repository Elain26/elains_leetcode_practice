class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyLinkedList(object):

    def __init__(self,val=0,next=None):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.size=0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        count=0
        p=self.head
        while p:
            if count==index:
                return p.val
            p=p.next
            count=count+1
        return -1
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_head=ListNode(val)
        new_head.next=self.head
        self.head=new_head
        self.size+=1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        p=self.head
        while p and p.next:
            p=p.next
        new_end=ListNode(val)
        p.next=new_end
        self.size+=1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        count=0
        cur=ListNode(val)
        p=self.head
        while p:            
            if count==index-1:
                p1=p.next
                p.next=cur
                cur.next=p1
                self.size+=1
            return self.head
            p=p.next
            count=count+1
        return 

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        count=0
        p=self.head
        while p:
            if count==index-1:
                p.next==p.next.next
            return self.head
            p=p.next
            count=count+1
        return 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
