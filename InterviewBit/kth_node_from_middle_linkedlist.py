# https://www.interviewbit.com/problems/kth-node-from-middle/
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        head, middle, cur = A, A, A
        mid_count = 0
        while not cur is None and not cur.next is None:
            middle = middle.next
            mid_count+=1
            cur = cur.next
            if not cur is None:
                cur = cur.next
            else:
                break

        if B>mid_count:
            return -1

        C = mid_count-B
        
        while C>0:
            head = head.next
            C-=1

        return head.val