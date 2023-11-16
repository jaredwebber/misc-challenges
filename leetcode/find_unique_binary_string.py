# https://leetcode.com/problems/find-unique-binary-string


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        ints: dict[int, bool] = {}
        for i in nums:
            ints[int(i, 2)] = True

        for i in range(0, 2 ** (len(nums))):
            if not ints.get(i):
                res: str = bin(i)[2:]
                return "0" * (len(nums) - len(res)) + res

        return ""
