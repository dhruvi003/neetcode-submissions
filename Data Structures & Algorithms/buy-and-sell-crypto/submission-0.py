class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1 
        gain = 0

        while r < len(prices):
            if prices[r]  > prices[l]:
                gain = max(gain, prices[r]-prices[l])
            else:
                l = r 

            r += 1 
        
        return gain