class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hs = [0]*26
        l = 0
        longest = 0

        for r in range(len(s)):
            hs[ord(s[r])-65] += 1 

            while (r-l+1) - max(hs) > k:
                
                hs[ord(s[l])-65] -= 1 
                l += 1 
            longest = max(longest, r-l+1)

        return longest
