class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        prefix_max = [0]*len(height)
        suffix_max = [0]*len(height)

        prefix_max[0] = height[0]
        for i in range(1,len(height)-1):
            prefix_max[i] = max(prefix_max[i-1], height[i])

        suffix_max[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            suffix_max[i] = max(suffix_max[i+1], height[i])

        for i in range(0, len(height)-1):
            left_max = prefix_max[i]
            right_max = suffix_max[i]

            if height[i] < left_max and height[i] < right_max:
                total += max(0,min(left_max, right_max) - height[i])

        return total