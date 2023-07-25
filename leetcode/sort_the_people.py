# https://leetcode.com/problems/sort-the-people


class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        combined: list[list[str, int]] = []
        for i in range(len(names)):
            combined.append([names[i], heights[i]])
        combined.sort(key=lambda x: -x[1])
        return [name for name, height in combined]
