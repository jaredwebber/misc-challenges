# https://leetcode.com/problems/hamming-distance


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        one = str(bin(x)[2:])
        two = str(bin(y)[2:])

        # pad with 0s
        if len(one) < len(two):
            one = ("0" * (len(two) - len(one))) + one
        elif len(two) < len(one):
            two = ("0" * (len(one) - len(two))) + two

        # calc score
        score: int = 0
        for i in range(len(one)):
            if one[i] != two[i]:
                score += 1

        return score
