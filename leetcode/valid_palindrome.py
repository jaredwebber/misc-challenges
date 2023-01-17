# https://leetcode.com/problems/valid-palindrome/description/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1

        while left < right:
            while not s[left].isalpha() and not s[left].isnumeric() and left < right:
                left += 1
            while not s[right].isalpha() and not s[right].isnumeric() and left < right:
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
