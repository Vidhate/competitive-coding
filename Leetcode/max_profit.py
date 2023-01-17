# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n<=1:
            return 0
            
        max_profit = 0
        buy, sell = prices[0], prices[0]
        for price in prices:
            if price<buy:
                buy = price
                sell = price
            
            elif price>buy:
                sell = price
                max_profit = max(max_profit, sell-buy)
                
        return max_profit