class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if self.minStack:
            if self.minStack[-1] > val:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)
            
    def pop(self) -> None:
        self.mainStack.pop()
        self.minStack.pop()   

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
