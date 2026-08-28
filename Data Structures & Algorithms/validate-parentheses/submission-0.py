class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) > 0:
                    peak = stack[-1]
                    if peak == '(' and c == ')':
                        stack.pop()
                    elif peak == '{' and c == '}':
                        stack.pop()
                    elif peak == '[' and c == ']':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) < 1