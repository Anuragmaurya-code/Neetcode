class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=1
        x=head
        while head:
            head=head.next
            count+=1
        
        toReach=count-n
        
        pointer=1
        while pointer<toReach-1:
            pointer+=1
            x=x.next
        if x.next:
            x.next=x.next.next
        return head
x=Solution()
print(x.removeNthFromEnd([1,2,3,4,5],2))