# https://leetcode.com/problems/reverse-bits/submissions/


class Solution:
    # n is int, not binary string
    # convert n to binary, reverse string, add 0s to pad 32 bits
    # return string converted to base 2 int
    def reverseBits(self, n: int) -> int:
        return int(("".join(reversed(bin(n)[2:]))) + "0" * (32 - len(bin(n)) + 2), 2)
