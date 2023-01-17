# https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for char in s:
            if char == "(":
                stack.append(")")
            elif char == "[":
                stack.append("]")
            elif char == "{":
                stack.append("}")
            elif len(stack) == 0 or stack.pop() != char:
                return False
        return len(stack) == 0
