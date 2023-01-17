# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		
		if len(prices)<=1:
            return 0
        
        max_profit = 0
        for i in range(1,len(prices)):
            diff = prices[i]-prices[i-1]
            max_profit = max_profit+diff if diff>0 else max_profit
        
        return max_profit