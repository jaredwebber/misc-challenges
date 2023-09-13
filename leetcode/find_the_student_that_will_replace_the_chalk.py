# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk


class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        index: int = 0
        total: int = 0

        for i in chalk:
            total += i

        k = k % total

        while k > 0:
            if k < chalk[index]:
                return index
            k -= chalk[index]
            index = (index + 1) % len(chalk)
        return index
