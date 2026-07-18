class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                j, h = stack.pop()
                w = i -j 
                max_area = max(max_area, w*h)
                start = j
            
            stack.append((start,height))
        
        while stack:
            j,h = stack.pop()
            max_area = max(max_area, (len(heights)-j)*h)
        
        return max_area

