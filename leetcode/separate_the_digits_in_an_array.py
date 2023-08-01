# https://leetcode.com/problems/separate-the-digits-in-an-array


class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        digits: list[int] = []
        for i in nums:
            if i > 9:
                val = str(i)
                for i in val:
                    digits.append(int(i))
            else:
                digits.append(i)
        return digits
