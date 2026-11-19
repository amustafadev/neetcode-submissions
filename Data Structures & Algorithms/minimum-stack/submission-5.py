class MinStack:

    # question had two pointers:
    # requires O(1) on all operations
    # `pop`, `top` and `getMin` will always be called on non-empty stacks.

    def __init__(self):
        self.stack = []
        # helper stack for min value operation on main stack
        # `min()`on a list is not O(1) 
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # at every push to main stack push/re-push the current minimum to minStack
        # lengths of both stack always stay equal
        # top element of minStack is the current minimum at any point
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # pop from both stack to maintain minimum
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
