# https://leetcode.com/problems/remove-element


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        shift: int = 0
        index: int = 0

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0 if nums[0] == val else 1

        while index < len(nums) - shift - 1:
            if nums[index] == val or nums[index] == -1:
                if nums[index] == val:
                    shift += 1
                nums[index] = nums[index + shift]
                nums[index + shift] = -1
            else:
                index += 1

        if (
            nums[index] == -1
            and nums[index + shift] != val
            and nums[index + shift] != -1
        ):
            nums[index] = nums[index + shift]
            nums[index + shift] = -1
            index += 1

        if nums[index] != val and nums[index] != -1:
            index += 1

        return index
