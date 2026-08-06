class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1 : 
            return heights[0]

        sett = {}

        heights = sorted(heights)
        res = 0
        for i in range(len(heights)) :
            if heights[i] in sett or heights[i]==0:
                continue
            
            res = max(res , heights[i] * (len(heights) - i ) )
        return res

        