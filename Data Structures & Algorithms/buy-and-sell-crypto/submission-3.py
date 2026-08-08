class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        #brute force way is a double for loop 

        #efficient way is a two pointer solution where every iteration you increase the right point and if the price[l] > price[r] then set l = r


        maxVal = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                maxVal = max(maxVal, prices[r] - prices[l])

            else:
                l = r
            r += 1
        return maxVal
        


