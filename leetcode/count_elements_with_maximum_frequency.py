# https://leetcode.com/problems/count-elements-with-maximum-frequency/


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        max_freq: int = 0
        freq_map: dict[int, int] = {}

        for i in nums:
            curr: int = freq_map.get(i, 0) + 1
            freq_map[i] = curr
            max_freq = max(max_freq, curr)

        total: int = 0
        for freq in freq_map.values():
            if freq == max_freq:
                total += max_freq

        return total


class SolutionTwo:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        nums.sort()

        last: int = -1
        max_freq: int = 0
        max_freq_count: int = 0
        curr_freq: int = 1

        for i in nums:
            if i == last:
                curr_freq += 1
            else:
                if curr_freq == max_freq:
                    max_freq_count += 1
                elif curr_freq > max_freq:
                    max_freq = curr_freq
                    max_freq_count = 1
                curr_freq = 1
            last = i

        if curr_freq > 1 and curr_freq == max_freq:
            max_freq_count += 1
        elif curr_freq > max_freq:
            max_freq = curr_freq
            max_freq_count = 1

        return max_freq * max_freq_count
