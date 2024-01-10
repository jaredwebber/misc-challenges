# https://leetcode.com/problems/find-common-characters


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        counts: dict[str, int] = {}
        curr_counts: dict[str, int] = {}
        updated_counts: dict[str, int] = {}

        for i in words[0]:
            counts[i] = counts.get(i, 0) + 1

        for i in range(1, len(words)):
            curr_counts = {}
            for i in words[i]:
                curr_counts[i] = curr_counts.get(i, 0) + 1

            updated_counts = {}
            for i in counts.keys():
                if curr_counts.get(i):
                    updated_counts[i] = min(counts.get(i), curr_counts.get(i))
            counts = updated_counts

        result: list[str] = []
        for char, count in counts.items():
            for i in range(count):
                result.append(char)

        return result
