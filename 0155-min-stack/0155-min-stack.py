class MinStack:

    def __init__(self):
        self.stack = [] 
        self.min = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min or value <= self.min[-1]:  
            self.min.append(value)


    def pop(self) -> None:
        value = self.stack.pop() 
        if value == self.min[-1]:
            self.min.pop()
         
        return value 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()