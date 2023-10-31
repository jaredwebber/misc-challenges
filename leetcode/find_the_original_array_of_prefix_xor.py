# https://leetcode.com/problems/find-the-original-array-of-prefix-xor


class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        prev: list[int] = pref[0]

        for i in range(1, len(pref)):
            pref[i] ^= prev
            prev ^= pref[i]

        return pref
