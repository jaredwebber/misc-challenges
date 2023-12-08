# https://leetcode.com/problems/rotate-string


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        goal_len: int = len(goal)
        goal_index: int = -1
        start_index: int = -1
        for i in range(goal_len):
            if goal[i] == s[0]:
                start_index = i
                goal_index = i
                for i in s:
                    if goal[goal_index] != i:
                        break
                    goal_index += 1
                    goal_index %= goal_len
                if goal_index == start_index:
                    return True

        return False
