# https://leetcode.com/problems/build-an-array-with-stack-operations


class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result: list[str] = []
        curr: int = 1

        for i in target:
            while curr < i:
                curr += 1
                result.append("Push")
                result.append("Pop")
            result.append("Push")
            curr += 1

        return result
