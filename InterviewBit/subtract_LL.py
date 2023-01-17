# https://www.interviewbit.com/problems/subtract/
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverse(self, head):
		p, c, n = None, head, None
		newhead = None
		while c:
			node = ListNode(c.val)
			node.next = p
			p = node
			c = c.next

		return p

	def subtract(self, A):
		l = 1
		h, mid = A, A
		fast, slow = A, A
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
		
		if fast:
			slow = slow.next
		self.printLL(slow)
		rev_list = self.reverse(slow)

		while rev_list:
			h.val = rev_list.val - h.val
			h = h.next
			rev_list = rev_list.next

		return A

	def printLL(self, h):
		while h:
			print(h.val, end=" ")
			h = h.next
		print()

	def createLL(self, l):
		head = ListNode(l[0])
		prev = head
		for e in l[1:]:
			node = ListNode(e)
			prev.next = node
			prev = prev.next

		return head

s = Solution()
ll = s.createLL([1,2,3,4,5])
s.printLL(ll)
s.printLL(s.subtract(ll))