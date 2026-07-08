class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+" , "-" , "*" , "/"]
        stack = []

        for i in range(len(tokens)):
            st = tokens[i]
            if st in ops:
                a = int(stack.pop())
                b = int(stack.pop())
                res = 0
                if st == "+":
                    res = a + b
                elif st == "-":
                    res = b-a
                elif st == "*":
                    res = a * b
                else:
                    res = b/a
                stack.append(res)
            else:
                stack.append(st)
        return int(stack[-1])

                