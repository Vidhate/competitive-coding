# https://www.interviewbit.com/problems/sort-binary-linked-list/

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    
    def solve(self, A):

        head, cur = A, A
        n1, n2 = 0, 0
        while not cur is None:
            if cur.val==1:
                n1+=1
            else:
                n2+=1
            cur = cur.next

        cur = head
        while n2>0:
            cur.val = 0
            cur = cur.next
            n2-=1

        while n1>0:
            cur.val = 1
            cur = cur.next
            n1-=1

        return head