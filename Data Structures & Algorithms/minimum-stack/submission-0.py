class MinStack:

    def __init__(self):
        self.stk = []        
        self.min_val = []

    def push(self, val: int) -> None:
        self.stk.append(val)

        if not self.min_val:
            self.min_val.append(val)
        elif self.min_val[-1] < val:
            self.min_val.append(self.min_val[-1])
        else:
            self.min_val.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.min_val.pop()
        
    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
        
