# https://leetcode.com/problems/largest-number-after-mutating-substring


class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        maximum: str = ""
        substr: int = 0
        for i in range(len(num)):
            if substr == 2:
                maximum += num[i]
            else:
                val: int = int(num[i])
                if change[val] >= val and (substr == 0 or substr == 1):
                    if change[val] != val:
                        substr = 1
                    maximum += str(change[val])
                else:
                    if substr == 1:
                        substr = 2
                    maximum += num[i]
        return maximum
