# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        curr = head
        if count == 1:
            return
        prev = head
        i = count - n
        
        if i == 0:
            return head.next

        while i:
            prev = curr
            curr = curr.next
            i -= 1
        
        prev.next = curr.next
        curr.next = None

        return head