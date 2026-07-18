class Solution:

    def canEat(self,piles, h, k):
        for item in piles:
            a = math.ceil(item/k)
            h -= a 
        if h>= 0:
            return True
        else:
            return False


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles) 
        l = 1
        r = max(piles)

        while l<= r:
            m = (l+r)//2

            if self.canEat(piles, h, m):
                ans = min(ans, m)
                r = m - 1 
            else:
                l = m + 1 
            
            # ans = min(ans, m)
        
        return ans
            
