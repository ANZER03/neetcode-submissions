class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1 : 
            return heights[0]

        maxA = 0
        stack = []

        for i , h  in enumerate(heights) :

            start = i

            while stack and stack[-1][1] > h :
                index, v = stack.pop()
                maxA = max (maxA, v * (i-index))
                start = index
            stack.append((start, h))

        # print(maxA)

        for ind , val in stack :
            maxA = max(maxA , val * ( len(stack) - ind))
        return maxA
                