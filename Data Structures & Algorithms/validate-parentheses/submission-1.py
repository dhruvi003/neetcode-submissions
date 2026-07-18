class Solution:
    def isValid(self, s: str) -> bool:
        lst = []

        for char in s:

            if char == ")":
                if lst and lst[-1] == "(":
                    lst.pop()
                else:
                    return False
            elif lst and char == "]":
                if lst[-1] == "[":
                    lst.pop()
                else:
                    return False 
            elif lst and char == "}":
                if lst[-1] == "{":
                    lst.pop()
                else:
                    return False 
            else:
                lst.append(char)

        return len(lst) == 0