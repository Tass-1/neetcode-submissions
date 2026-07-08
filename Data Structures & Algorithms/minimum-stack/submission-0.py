class MinStack:
    
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val , val))
        else:
            curr = self.stack[-1][1]
            nm = min(val , curr)
            self.stack.append((val , nm))

    def pop(self) -> None:
        s = self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
