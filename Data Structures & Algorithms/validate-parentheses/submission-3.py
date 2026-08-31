class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if len(stack) < 1:
                    return False
                else:
                    if s[i] == ')' and stack[-1] == '(':
                        stack.pop()
                    elif s[i] == '}' and stack[-1] == '{':
                        stack.pop()
                    elif s[i] == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        return len(stack) < 1
