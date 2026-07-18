class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = {}
        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord('a')] += 1 

            key = tuple(count)

            if key in hs:
                hs[key].append(s)
            else:
                hs[key] = [s]
        
        return list(hs.values())
