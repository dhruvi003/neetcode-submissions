class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []
        for item in operations:
            
            if item == '+':
                lst.append(lst[-1]+lst[-2])
            elif item == 'C':
                lst.pop()
            elif item == "D":
                lst.append(lst[-1]*2)
            else:
                lst.append(int(item))
        
        return sum(lst)