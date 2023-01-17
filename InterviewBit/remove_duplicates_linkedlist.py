# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):

		head = A
		p, c, n = None, A, A.next
		dup = False

		while n and n.val==c.val:
			n = n.next
			dup = True
		if dup:
			if prev is None:
				prev = n
			else:
				prev.next = n
			c = n
			n = n.next
			dup = False
		else:
			prev = c
			c = n
			n = n.next


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
ll = s.createLL([2,2,2,1,1,1])
s.printList(ll)
s.printList(s.deleteDuplicates(ll))