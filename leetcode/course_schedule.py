# https://leetcode.com/problems/course-schedule/description/


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list: dict[list[int]] = {}
        for p in prerequisites:
            if not adj_list.get(p[0]):
                adj_list[p[0]] = []
            adj_list.get(p[0]).append(p[1])

        visited: dict[int] = {}
        for i in range(numCourses):
            if self.not_possible(adj_list, i, visited):
                return False

        return True

    def not_possible(
        self, graph: dict[list[int]], course: int, visited: dict[int]
    ) -> bool:
        if visited.get(course) == -1:
            return True
        if visited.get(course) == 1:
            return False

        visited[course] = -1

        not_possible: bool = False
        for i in graph.get(course) if graph.get(course) else []:
            not_possible = not_possible or self.not_possible(graph, i, visited)

        visited[course] = 1

        return not_possible
