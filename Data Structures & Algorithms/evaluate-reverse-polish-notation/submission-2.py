class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token != '+' and token != '-' and token != '*' and token != '/':
                stack.append(int(token))
                continue
            
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                val = a + b
            elif token == '-':
                val = a - b
            elif token == '*':
                val = a * b
            else:
                val = int(a / b)
            
            stack.append(val)

        return stack.pop()