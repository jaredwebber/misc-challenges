# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/description/


class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        distinct: set = set()

        for i in nums:
            distinct.add(i)
            curr: str = str(i)
            reverse: str = ""
            for c in range(len(curr) - 1, -1, -1):
                reverse += curr[c]
            distinct.add(int(reverse))

        return len(distinct)
