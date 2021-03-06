class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#注意题目里给的index是从0开始的，第一个数的index是0
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        #这个size超重要的，要用来排除掉invalid的index，一定要记得定义一个
        self.size=0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        p=self.head
        if index>self.size-1 or index<0:
            return -1
        for i in range(index+1):
            if i==index:
                return p.val
            p=p.next
            i+=1
        
    
        

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
        new_tail=ListNode(val)
        #特殊情况，如果前面没有valid的Node，那么addAtTail和addAtHead其实一样
        if self.size==0:
            self.head=new_tail
            self.size+=1
            return
        while p.next:
            p=p.next
        p.next=new_tail
        self.size+=1
            
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index>self.size:
            return
        add_node=ListNode(val)
        p=self.head
        #特殊情况，当index为0的时候相当于addAtHead
        if index==0:
            new_head=ListNode(val)
            new_head.next=self.head
            self.head=new_head
            self.size+=1
            return
        for i in range(index):
            if i==index-1:
                p0=p.next
                p.next=add_node
                add_node.next=p0
            p=p.next
        self.size+=1        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        p=self.head
        #如果index超出size的情况就不删了
        if index>self.size-1:
            return
        #特殊情况，如果index为0的话直接把head去掉
        if index==0:
            p=p.next
            self.head=p
            self.size-=1
            return
        for i in range(index):
            if i==index-1:
                p.next=p.next.next
            p=p.next
        self.size-=1

# Your MyLinkedList object will be instantiated and called as such:

obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
p0=obj.addAtIndex(1,2)
#print(p0.val,p0.next.val,p0.next.next.val)
param_1 = obj.get(1)
p0=obj.deleteAtIndex(1)
print(p0.val,p0.next.val)
param_2 = obj.get(1)
print(param_2)
