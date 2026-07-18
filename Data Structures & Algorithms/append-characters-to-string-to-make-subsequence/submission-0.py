class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        j = 0

        for char in s:
            if j < n and t[j] == char:
                j += 1 
        
        return n-j