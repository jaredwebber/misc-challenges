# https://leetcode.com/problems/sort-array-by-increasing-frequency/


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq_map: dict[int, int] = {}
        for i in nums:
            freq_map[i] = freq_map.get(i, 0) + 1

        map_list: list[tuple] = []
        for val, count in freq_map.items():
            map_list.append((val, count))

        map_list.sort(key=lambda x: (x[1], -x[0]))

        result: list[int] = []
        for val, count in map_list:
            result.extend([val for _ in range(count)])

        return result
