class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "*":
                m1 = stack.pop()
                m2 = stack.pop()
                p1 = m1 * m2 
                stack.append(p1)
            elif  i == "+":
                m1 = stack.pop()
                m2 = stack.pop()
                p1 = m1 + m2 
                stack.append(p1)
            elif i == "-":
                m1 = stack.pop()
                m2 = stack.pop()
                p1 = m2 - m1
                stack.append(p1)
            elif i == "/":
                m1 = stack.pop()
                m2 = stack.pop()
                p1 = int (m2 / m1)
                stack.append(p1)
            else:
                stack.append(int(i))

        return stack[-1]