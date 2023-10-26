# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits


class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        sum_values: int = 0

        for i in range(len(nums)):
            binary: str = bin(i)[2:]

            if len(binary) >= k:
                set_bits: int = binary.count("1")

                if set_bits == k:
                    sum_values += nums[i]

        return sum_values
