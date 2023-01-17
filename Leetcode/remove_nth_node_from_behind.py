# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast, slow, prev = head, head, None
        pos = 0
        while fast and pos<n:
            fast = fast.next
            pos+=1
        
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
            
        if not prev and not slow.next:
            return None
        
        if not prev and slow.next:
            return head.next
        
        prev.next = slow.next
        slow.next = None
        
        return head