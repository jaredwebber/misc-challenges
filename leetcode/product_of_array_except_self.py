# https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        arr: list[int] = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            arr[i] = nums[i - 1] * arr[i - 1]

        prod: int = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            arr[i] *= prod

        return arr
