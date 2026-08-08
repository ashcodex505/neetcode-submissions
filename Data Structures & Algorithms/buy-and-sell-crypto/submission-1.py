class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #We basically have our left and right pointer start at index 0 and then 0+1
        l = 0
        r = l + 1
        maxVal = 0


        while r < len(prices):
  
            if prices[l] < prices[r]:
                maxVal = max(maxVal, prices[r] - prices[l]) 
            else:
                l = r
            r += 1
        return maxVal


