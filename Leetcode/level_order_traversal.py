# aka BFS in Binary Trees
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if not root:
			return []
		if not root.left and not root.right:
			return [[root.val]]

		queue_current, queue_next = [root], []
		answer = []
		while len(queue_current)>0:

			level_values = []
			while len(queue_current)>0:
				node = queue_current.pop(0)
				level_values.append(node.val)
				#print(node.val, end=" ")

				if node.left:
					queue_next.append(node.left)
				if node.right:
					queue_next.append(node.right)

			#print()
			answer.append(level_values)
			queue_current = queue_next.copy()
			queue_next = []

		return answer

		

# [3,9,20,null,null,15,7]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print(s.levelOrder(TreeNode(5)))

