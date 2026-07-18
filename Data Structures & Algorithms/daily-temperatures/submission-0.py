class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        result = [0] * len(temp)
        stack = []
        
        for index, item in enumerate(temp):
            while stack and stack[-1][1] < item:
                curr_idx, curr_item = stack.pop()
                result[curr_idx] = index - curr_idx

            stack.append((index, item))
            
        return result
        