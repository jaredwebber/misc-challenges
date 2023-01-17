# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
