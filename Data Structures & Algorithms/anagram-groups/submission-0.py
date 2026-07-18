class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = {}
        for s in strs:
            a = str(sorted(s))
            if a in hs:
                hs.get(a).append(s)
            else:
                hs[a] = [s]
        ls = []
        for k in hs.keys():
            ls.append(hs.get(k))
        return ls