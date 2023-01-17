# https://leetcode.com/problems/max-area-of-island/
from typing import List
class Solution:

	def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
		ans, R, C = 0, range(len(grid)), range(len(grid[0]))  # <-- initialize some stuff for maxAreaOfIsland
		
		def explore(r: int, c: int)->int:                     # <-- The recursive function
			grid[r][c], res, dr, dc = -1, 0, 1, 0             # <-- dr, dc = 1,0 sets the initial direction as south

			for _ in range(4):
				row, col = r+dr, c+dc
				if row in R and col in C and grid[row][col] == 1:
					res+= explore(row, col)
					
				dr, dc = dc, -dr                          # <--- this transformation rotates the direction though the 
															  # sequence south, west, north, east
			return res+1      
		
		for r in R:                                           # <--- the iteration through the grid
			for c in C:
				if grid[r][c] >= 1:
					ans = max(explore(r,c), ans)       
		return ans


s = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(s.maxAreaOfIsland(grid))