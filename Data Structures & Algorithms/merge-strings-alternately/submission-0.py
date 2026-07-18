class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        i =0
        while i < min(len(word1), len(word2)):
            lst.append(word1[i])
            lst.append(word2[i])
            i += 1 
        
        if len(word1) > len(word2):
            lst.append(word1[i:])
        elif len(word1) < len(word2):
            lst.append(word2[i:])

        return ''.join(lst)