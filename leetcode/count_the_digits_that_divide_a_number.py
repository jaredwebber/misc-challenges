# https://leetcode.com/problems/count-the-digits-that-divide-a-number


class Solution:
    def countDigits(self, num: int) -> int:
        count: int = 0
        digits: list[int] = [int(i) for i in str(num)]
        for i in digits:
            if num % i == 0:
                count += 1
        return count
