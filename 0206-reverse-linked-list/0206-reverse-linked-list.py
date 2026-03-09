# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        last = head

        now = head.next
        head.next = None

        while now:
            temp = now.next
            now.next = last
            last = now

            now = temp
        return last
