# https://www.interviewbit.com/problems/red-zone/
import pprint
class Solution:
	# @param A : list of list of integers
	# @param B : integer
	# @return an integer

	def dist(self, p1, p2):
		return (((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))**0.5

	def approx(self, d):
		return int(d)+1 if d-int(d)>0 else int(d)
		#return (d)

	def find_intersection(self, c1, c2, r):
		center_dist = self.dist(c1, c2)
		if center_dist>2*r:
			return []

		mid = [(c1[0]+c2[0])/2, (c1[1]+c2[1])/2]

		if center_dist==2*r:
			return [mid]

		h = ((r**2) - (center_dist**2/4))**0.5
		int1 = [( mid[0] + ((c2[1]-c1[1])*(h/center_dist)) ), ( mid[1] - ((c2[0]-c1[0])*(h/center_dist)) )]
		int2 = [( mid[0] - ((c2[1]-c1[1])*(h/center_dist)) ), ( mid[1] + ((c2[0]-c1[0])*(h/center_dist)) )]
		return [int1, int2]


	def find_all_intersections(self, A, days, B):
		
		points = []
		for i in range(len(A)):
			p1 = A[i]
			for j in range(i+1,len(A)):
				p2 = A[j]
				points = self.find_intersection(p1, p2, days)
				if len(points)==0:
					continue
				else:
					ozone1, ozone2 = 2, 2

					for k in range(j+1, len(A)):
						d1 = self.dist(A[k], points[0])
						if round(d1,4)<days:
							ozone1+=1
							if ozone1>=B:
								return True

						if len(points)>1:
							d2=self.dist(A[k], points[1])
							if round(d2,4)<days:
								ozone2+=1
								if ozone2>=B:
									return True
			
		return False

	def possible_redzone(self, points, A, days, B):

		if len(points)==0:
			return False

		for point in points:
			orange_zones = 0
			#print(point, end=" ")
			for p in A:
				d = self.dist(point, p)
				#print(d, end=" ")
				if round(d,4)<=(days):
					orange_zones+=1

				if orange_zones>=B:
					return True

		return False


	def solve(self, A, B):
		x, y = 0 , 0
		x_min, x_max = A[0]
		y_min, y_max = A[0]

		for point in A:
			x+=point[0]
			y+=point[1]

			x1, y1 = point
			x_min = x1 if x1<x_min else x_min
			y_min = y1 if y1<y_min else y_min
			x_max = x1 if x1>x_max else x_max
			y_max = y1 if y1>y_max else y_max

		#print(points)

		#x, y = x//len(A), y//len(A)
		#mid_point = [x,y]

		min_d, max_d = 0, self.approx(self.dist([0, 0], [x_max, y_max]))
		mini_days = (max_d)
		while min_d<=max_d:

			days = (min_d+max_d)//2
			#points = self.find_all_intersections(A, days)
			#print(points, min_d, max_d, days)
			#possible = self.possible_redzone(points, A, days, B)
			#print(possible)
			possible = self.find_all_intersections(A, days, B)

			if possible:
				if days<mini_days:
					mini_days=days
				max_d = days - 1
			else:
				min_d = days + 1


		return int(mini_days)


#A, B = [[8, 5],[0, 4],[3, 6],], 3
A, B = [[2, 3], [9, 4], [10, 3]], 2
#A, B = [[6, 3], [7, 10], [2, 8], [5, 6], [1, 10]], 2
#A, B = [[10,6], [5,7]], 2
"""
A = [
  [762888, 842056],
  [943296, 205226],
  [528530, 840859],
  [490975, 305681],
  [784949, 795242],
  [364631, 24977],
  [335193, 566499],
  [175628, 435361],
  [394134, 454625],
  [130339, 131963],
  [62547, 401942],
  [101919, 622627],
  [667354, 263679],
  [704772, 951888],
  [183983, 927405],
  [192090, 610510],
  [573528, 118235],
  [156736, 580620],
  [507137, 194840],
  [665701, 508127],
  [26162, 42107]
]
B = 20
#"""

s = Solution()
print(s.solve(A,B))