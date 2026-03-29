class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # Start with a very high number
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            current_price = price - min_price

            if current_price > max_profit:
                max_profit = current_price
        
        return max_profit