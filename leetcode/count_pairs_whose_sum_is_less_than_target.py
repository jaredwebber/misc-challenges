# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target


class BruteForceSolution:
    def countPairs(self, nums: list[int], target: int) -> int:
        count: int = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count
