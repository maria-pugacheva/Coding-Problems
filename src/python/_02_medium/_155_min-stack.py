# Time Complexity : O(1) for all operations. Space Complexity : O(n)
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = val
        if self.stack:
            curr_min = min(curr_min, self.stack[-1][1])
        self.stack.append([val, curr_min])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


stack = MinStack()
stack.push(3)
stack.push(-1)
stack.push(4)
stack.push(2)
stack.pop()
print(stack.getMin() == -1)
