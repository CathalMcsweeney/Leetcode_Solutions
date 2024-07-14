class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
                continue
            elif char == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
            elif char == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
            elif char == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
            else:
                return False
            stack.pop()     
        if len(stack) > 0:
            return False
        return True

solution = Solution()

s = "([)]"
print(solution.isValid(s))

s = "()[]"
print(solution.isValid(s))

s = "(("
print(solution.isValid(s))