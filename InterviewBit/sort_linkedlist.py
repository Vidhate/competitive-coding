# https://www.interviewbit.com/problems/sort-list/

# Need to implement mergesort to have an O(nlogn) solution

#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def findpos(self, head, val):
		p = 0
		while head and head.val<val:
			head = head.next
			p+=1

		return p

	def insert(self, head, pos, val):
		node = ListNode(val)
		if pos==0:
			node.next = head
			return node

		prev, cur = head, head.next
		p = 1
		while cur and p<pos:
			prev = cur
			cur = cur.next
			p+=1
		
		prev.next = node
		node.next = cur
		return head

	def merge(self, lefthead, righthead):
		right = righthead
		while right:
			pos = self.findpos(lefthead, right.val)
			lefthead = self.insert(lefthead, pos, right.val)
			right = right.next

		return lefthead

	def splitLL(self, head):
		fast, slow, prevslow = head, head, None
		while fast and fast.next:
			prevslow = slow
			slow = slow.next
			fast = fast.next.next

		prevslow.next = None
		return head, slow

	def mergesort(self, head):

		if not head.next:
			return head

		left, right = self.splitLL(head)
		
		left = self.mergesort(left)
		
		right = self.mergesort(right)
		
		sorthead = self.merge(left, right)
		# self.printList(left)
		# self.printList(right)
		# self.printList(left)
		# self.printList(right)
		# self.printList(sorthead)
		# print("\n\n\n")

		return sorthead
		
	def sortList(self, A):
		return self.mergesort(A)

	# Function to insert a new node at the beginning
	def push(self, new_data, head):
		new_node = ListNode(new_data)
		new_node.next = head
		return new_node
 
	# Utility function to print the linked LinkedList
	def printList(self, head):
		temp = head
		while(temp):
			print(temp.val, end = " ")
			temp = temp.next
		print()


	def createLL(self, nums):
		head = None
		for num in nums:
			head = self.push(num, head)

		return head

s = Solution()
ll = s.createLL([1,2,3,4,5])
# s.printList(ll)
# l, r = s.splitLL(ll)
# s.printList(l)
# s.printList(r)
s.sortList(ll)
