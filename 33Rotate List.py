class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
node1=ListNode(0)
node2=ListNode(1)
node3=ListNode(2)
node1.next=node2
node2.next=node3
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #特殊情况，链表空的返回空
        if head is None:
            return 
        #特殊情况，链表只有一个数，转多少次都一样
        if head.next is None or k==0:
            return head
        #计算链表长度
        p=head
        linkLen=0
        while p:
            p=p.next
            linkLen+=1
        #旋转次数等于链表长度或能被链表长整除，则不需要旋转
        if k==linkLen or k%linkLen==0:
            return head
        #旋转次数比链表长度大，可以取个余数
        #不需要一次一次旋转，只要找到断开重连的点就行
        #这里断开的点编号为breakNode，（从1开始计数）
        if k>linkLen:
            breakNode=linkLen-(k%linkLen)
        if k<linkLen:
            breakNode=linkLen-k
        print(k,breakNode,linkLen)
        #指针指向需要断开的节点
        p=head
        i=1
        while i!=breakNode:
            p=p.next
            i+=1
        #该节点成为新的head
        new_head=p.next
        p2=new_head
        #新建p2指针，沿着该节点走到原末尾
        while p2.next:
            p2=p2.next
        #将断开点前一个点的next设为none，即创造新末尾
        p.next=None
        #然后把新head的末尾与原head相连
        p2.next=head
        
        return new_head
a=Solution()
head=a.rotateRight(node1,4)
print(head.val)
