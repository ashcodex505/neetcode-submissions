class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #BRUTE FORCE
        res = 0 
        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                area = (r-l) * min(heights[r], heights[l])
                if area > res:
                    res = area
        return res
                
        
        