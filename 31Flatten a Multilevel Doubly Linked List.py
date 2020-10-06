"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
#recursion is so hard to understand, so I chose not to use it
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        node=head
        while node:
            if node.child:
                #remember the node that has node.child
                nextstart=node
                #append the second level link to the level 1 link
                self.appendlist(node)
                #put the node back to where we begin
                #yeah this backwrad a bit, but it's easy to understand
                node=nextstart.next
            else:
                node=node.next
        return head
    #input the node that has node.child,add the rest of the link of this layer to the level 1 link
    #no need to care about if there's any node.child exist in this link, we will fix it later
    def appendlist(self,node):
        next_node=node.next
        node.next=node.child
        node.next.prev=node
        node.child=None
        while node.next:
            node=node.next
        node.next=next_node
        if next_node:
            next_node.prev=node
        return 
                
