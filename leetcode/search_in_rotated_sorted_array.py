# https://leetcode.com/problems/search-in-rotated-sorted-array/description/


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        mid: int = 0

        while left < right:
            mid = int((right + left) / 2)
            print(str(left) + ", " + str(mid) + ", " + str(right))
            if target == nums[mid]:
                return mid
            if nums[left] < nums[right]:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[left] > nums[mid]:
                    if target < nums[left] and target > nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if target < nums[left] or target > nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1

        return left if nums[left] == target else right if nums[right] == target else -1
