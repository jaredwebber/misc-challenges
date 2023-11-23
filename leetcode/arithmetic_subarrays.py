# https://leetcode.com/problems/arithmetic-subarrays


class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:  # noqa: E741
        out: list[bool] = []

        for i in range(len(l)):
            if r[i] - l[i] < 2:
                out.append(True)
            else:
                sub_arr = list(nums[l[i] : r[i] + 1])  # noqa: E203
                sub_arr.sort()
                diff: int = sub_arr[1] - sub_arr[0]
                last: int = sub_arr[0]
                arithmetic: bool = True

                for j in range(1, len(sub_arr)):
                    if sub_arr[j] - diff != last:
                        arithmetic = False
                        break
                    last = sub_arr[j]
                out.append(arithmetic)

        return out
