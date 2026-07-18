class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        prev_max = 0
        while l<r:
            w = min(heights[l],heights[r]) * (r-l)
            prev_max = max(prev_max, w)
            if heights[l] < heights[r]:
                l += 1 
            else:
                r -= 1
        return prev_max