class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string 
        return res

    def decode(self, s: str) -> List[str]:
        # 3#hey2#hi 
        ls = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 
            
            lenn = int(s[i:j])
            stt = s[j+1 : j+1+lenn]
            ls.append(stt)

            i = j + 1 + lenn
        
        return ls


