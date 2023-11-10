# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs


class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        adjacency_list: dict[int, list[int]] = {}

        for i, j in adjacentPairs:
            i_list = adjacency_list.get(i, list())
            i_list.append(j)
            adjacency_list[i] = i_list

            j_list = adjacency_list.get(j, list())
            j_list.append(i)
            adjacency_list[j] = j_list

        used: set[int] = set()
        result: list[int] = []
        for value, attached in adjacency_list.items():
            if len(attached) == 1:
                used.add(value)
                result.append(value)
                children: list[int] = attached

                while len(result) < len(adjacentPairs) + 1:
                    for i in children:
                        if i not in used:
                            used.add(i)
                            result.append(i)
                    children = adjacency_list[result[-1]]
                break

        return result
