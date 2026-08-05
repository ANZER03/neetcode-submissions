class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0 , len(height) - 1
        maxA = 0
        while l < r :
            # print(f"r : {r} , l : {l}")
            maxA = max( maxA , min(height[l] , height[r]) * (r-l) )

            if height[l] - height[r] > 0 :
                r -= 1
            else :
                l += 1
        
        return maxA

