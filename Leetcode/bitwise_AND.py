# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Find first mismatching bit from left - all bitwise ANDs after this point will lead to zero because the lower number will cross through 100000... to reach the higher number and since there's a mismatch the current bitwise AND is already 0

class Solution:
	def rangeBitwiseAnd(self, left: int, right: int) -> int:
		
        if left==0 or right==0:
            return 0
        if left==right:
            return left
        
        tracker = 2**31
        answer = 0
        for i in range(31):
            left_bit, right_bit = left//tracker, right//tracker
            left %= tracker
            right %= tracker
            
            if left_bit!=right_bit:
                return int(answer)
                
            elif left_bit==1 and right_bit==1:
                answer+=tracker
            
            tracker/=2
            
        return int(answer)