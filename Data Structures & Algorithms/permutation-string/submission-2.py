class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_1 = 26 * [0]
        counts_2 = 26 * [0]

        for c in s1:
            counts_1[ord(c)-97] += 1 
        
        l = 0
        for r in range(len(s2)):
            while r - l + 1 > len(s1):
                counts_2[ord(s2[l])-97] -= 1 
                l += 1 
            
            counts_2[ord(s2[r])-97] += 1 

            if counts_1 == counts_2:
                return True 

        return False
                