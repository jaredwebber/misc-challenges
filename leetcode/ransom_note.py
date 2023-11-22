# https://leetcode.com/problems/ransom-note


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_map: dict[str, int] = {}
        for i in magazine:
            mag_map[i] = mag_map.get(i, 0) + 1

        for i in ransomNote:
            if mag_map.get(i, 0) == 0:
                return False
            else:
                mag_map[i] -= 1

        return True
