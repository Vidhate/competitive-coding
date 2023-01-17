# https://leetcode.com/problems/sudoku-solver/
from typing import List
class Solution:
	def noSets(self, board):
		for i in range(9):
			for j in range(9):
				if len(board[i][j])>1 or board[i][j]=='.':
					return False
		return True

	def printBoard(self, board):
		for i in range(9):
			for j in range(9):
				print(board[i][j], end=" ")
			print()
		print("\n"*2)

	def solveSudoku(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
		
		full_set = set([1,2,3,4,5,6,7,8,9])
		rows, cols, sections = [], [], []
		for i in range(9):
			row, col = [int(r) for r in board[i] if not r=='.'], [int(c[i]) for c in board if not c[i]=='.']
			section = []

			down, side = (i//3)*3, (i%3)*3
			for j in range(down, down+3):
				for k in range(side, side+3):
					if board[j][k]!='.':
						section.append(int(board[j][k]))

			rows.append(row)
			cols.append(col)
			sections.append(section)

		self.printBoard(board)

		rows_possible, cols_possible, sections_possible = {}, {}, {}
		while not self.noDots(board):
			for i in range(9):
				row_possible = []
				for j in range(9):
					if len(board[i][j])>1 or board[i][j]=='.':
						section = int(((i//3)*3)+(j//3))
						possible = full_set - set(rows[i]) - set(cols[j]) - set(sections[section])

						if len(possible)==1:
							element = list(possible)[0]
							board[i][j] = str(element)
							rows[i].append(element)
							cols[j].append(element)
							sections[section].append(element)
						else:
							row_possible.append(possible)

			self.printBoard(board)
			print(rows)
			print(cols)
			print(sections)
			print('-'*15)

s = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
print(s.solveSudoku(board))