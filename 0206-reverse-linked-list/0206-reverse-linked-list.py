# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next

        arr = arr[::-1]
        cur = head
        i = 0
        while cur:
            cur.val = arr[i]
            i += 1
            cur = cur.next

        return head
