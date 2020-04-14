class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.t=-1

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.t+=1

    def pop(self) -> None:
        self.stack.pop()
        self.t-=1

    def top(self) -> int:
        x=self.stack[self.t]
        
        return x

    def getMin(self) -> int:
        x=min(self.stack)
        i=self.stack.index(x)
        m = self.stack[i]
        
        return m


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
print(minStack.t)
minStack.pop()
print(minStack.t)

print(minStack.stack)
print(minStack.top())    
print(minStack.getMin())
