# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        odd = head

        even = head.next
        
        even_head = even
        cur = even.next
        i = 1
        while cur:
            if i%2 == 1:
                odd.next = cur
                odd = odd.next
                cur = cur.next
                i += 1
            else:
                even.next = cur
                even = even.next
                cur = cur.next
                i += 1
        even.next = None
        odd.next = even_head

        return head


