# https://leetcode.com/problems/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq: dict[int] = {}
        for i in nums:
            freq[i] = (i, freq.get(i)[1] + 1 if freq.get(i) is not None else 1)

        tuples = list(freq.values())
        tuples.sort(key=lambda a: a[1], reverse=True)

        out = []
        for i in tuples:
            out.append(i[0])
            if len(out) == k:
                return out


class SolutionTwo:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map: dict[int, int] = {}
        for i in nums:
            freq_map[i] = freq_map.get(i, 0) + 1

        frequencies: list[list[int]] = sorted(list(freq_map.items()), key=lambda x: -x[1])

        results: list[int] = []
        for i in range(k):
            results.append(frequencies[i][0])

        return results
