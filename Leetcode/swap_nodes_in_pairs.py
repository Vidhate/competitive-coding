# https://leetcode.com/problems/swap-nodes-in-pairs/
# st - 8:49; en - 9:00;

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None

        prev, cur, nxt = None, head, head.next
        while cur and nxt:
            cur.next = nxt.next
            nxt.next = cur
            if not prev is None:
                prev.next = nxt
            else:
                head = nxt

            prev = cur
            cur = cur.next
            if cur is None:
                break
            nxt = cur.next
        return head
