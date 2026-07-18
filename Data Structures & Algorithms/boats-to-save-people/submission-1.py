class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        i,j = 0, len(people)-1 
        boats = 0

        while i <= j:
            
            if i == j:
                boats += 1
                break
            
            s = people[i] + people[j]
            if s <= limit:
                
                boats += 1 
                i += 1 
                j -= 1 
            else:
                
                boats += 1
                j -= 1 
    
        return boats