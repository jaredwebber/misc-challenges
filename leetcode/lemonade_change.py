# https://leetcode.com/problems/lemonade-change


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        bill_count: list[int] = [0, 0]
        for i in bills:
            if i == 5:
                bill_count[0] += 1
            elif i == 10:
                bill_count[0] -= 1
                bill_count[1] += 1
            elif i == 20:
                if bill_count[1] > 0:
                    bill_count[0] -= 1
                    bill_count[1] -= 1
                else:
                    bill_count[0] -= 3

            if bill_count[0] < 0 or bill_count[1] < 0:
                return False

        return True
