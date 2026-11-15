class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):

            if s[i] == ']' or s[i] == ')' or s[i] == '}':
                
                print(s)

                if len(stack) == 0:
                    return False
            
                last = stack[-1]

                if (last == '[' and s[i] == ']') or \
                    (last == '(' and s[i] == ')') or \
                    (last == '{' and s[i] == '}'):

                    stack.pop()
                
                else:
                    return False

            else:
                stack.append(s[i])

        return len(stack) == 0