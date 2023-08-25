# https://leetcode.com/problems/number-of-senior-citizens


class Solution:
    def countSeniors(self, details: list[str]) -> int:
        seniors: int = 0
        for i in details:
            if int(i[11:13]) > 60:
                seniors += 1
        return seniors
