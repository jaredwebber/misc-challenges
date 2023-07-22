# https://leetcode.com/problems/find-maximum-number-of-string-pairs


class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        sort: dict[str] = {}
        count: int = 0
        for i in words:
            sort_str = "".join(sorted(i))
            if sort.get(sort_str):
                count += 1
                sort.pop(sort_str)
            else:
                sort[sort_str] = 1
        return count
