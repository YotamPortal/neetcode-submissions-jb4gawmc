class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            maxWidth = r - l
            maxHeight = min(heights[l], heights[r])
            maxArea = max(maxArea, maxWidth * maxHeight)
            if heights[l] < heights[r]:
                l += 1
            else: # heights[l] >= heights[r]:
                r -= 1
        return maxArea