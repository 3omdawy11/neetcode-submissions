# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        curr = head
        nxt = None
        if curr:
            nxt = curr.next

        while nxt:

            if curr == nxt:
                return True
            
            curr = curr.next
            if nxt.next and nxt.next.next:
                nxt = (nxt.next).next
            else:
                break
        
        return False
        