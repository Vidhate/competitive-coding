from typing import List
class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		
		course_map = {pre[0]:pre[1] for pre in prerequisites}
		if len(prerequisites)==0:
			return True
		
		course_stack = []
		course = list(course_map.keys())[0]
		print(course_map)
		while course_map:
			if course_map.get(course,-1)==-1:
				for c in course_stack:
					course_map.pop(c)
				course_stack = []
				print(course_map)
					
			elif course in course_stack:
				return False
			
			else:
				course_stack.append(course)
				course = course_map[course]
				print(course_stack)
				continue
				
			if len(list(course_map.keys()))==0:
				break
			course = list(course_map.keys())[0]
			
		if course_map:
			return False
		return True

s = Solution()
#print(s.canFinish(1, []))
print(s.canFinish(3, [[1,0],[1,2],[0,1]]))