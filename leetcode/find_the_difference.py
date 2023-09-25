# https://leetcode.com/problems/find-the-difference


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_arr = list(s)
        s_arr.sort()
        t_arr = list(t)
        t_arr.sort()

        for i in range(len(s_arr)):
            if s_arr[i] != t_arr[i]:
                return t_arr[i]

        return t_arr[len(t_arr) - 1]
