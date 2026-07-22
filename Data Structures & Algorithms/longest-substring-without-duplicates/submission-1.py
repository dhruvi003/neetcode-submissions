class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        ll = 0 
        ss = set()

        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l += 1
            ss.add(s[r]) 
            ll = max(ll, (r-l)+1)

        return ll