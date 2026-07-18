class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []
        for item in tokens:
            if item not in "+/*-":
                lst.append(int(item))
            else:
                if lst:
                    a = lst.pop()
                    b = lst.pop()

                if item == "+":
                    lst.append(a+b)
                elif item == "*":
                    lst.append(a*b)
                elif item == "-":
                    lst.append(b-a)
                elif item == "/":
                    lst.append(int(b/a))
        return lst[0]