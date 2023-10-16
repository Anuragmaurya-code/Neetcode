# Definition for singly-linked list.
class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        head=ListNode()
        for list in lists:
            x=head
            while list:
                while True:
                    if x.next==None or x.next.val>=list.val:
                        node=list
                        list=list.next
                        node.next=x.next
                        x.next=node
                        break
                    else:
                        x=x.next
        return head.next
q=[]
c=ListNode(5)
b=ListNode(4,c)
a=ListNode(1,b)
q.append(a)

c=ListNode(4)
b=ListNode(3,c)
a=ListNode(1,b)
q.append(a)

b=ListNode(2)
a=ListNode(6,b)
q.append(a)

x=Solution()
s=x.mergeKLists(q)
while s:
    print(s.val)
    s=s.next






