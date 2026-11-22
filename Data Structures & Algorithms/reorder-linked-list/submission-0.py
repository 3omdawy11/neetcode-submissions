# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return

        counter = 0
        curr = curr2 = head

        # Count
        while curr2:
            counter += 1
            curr2 = curr2.next

        mid = (counter // 2) + 1

        # Walk to the last node of the first half, then cut
        counter = 0
        curr2 = head
        while counter < mid - 1:
            curr2 = curr2.next
            counter += 1
        first_tail = curr2
        curr2 = curr2.next
        first_tail.next = None

        # Reverse second half
        prev = None
        while curr2:
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp
        curr2 = prev

        # Merge
        while curr and curr2:
            temp = curr.next
            temp2 = curr2.next

            curr.next = curr2
            curr2.next = temp
            curr = temp
            curr2 = temp2


        

            

        