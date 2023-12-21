# https://leetcode.com/problems/keys-and-rooms


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited: set[int] = set()

        queue: list[int] = rooms[0]
        visited.add(0)

        while len(queue) > 0:
            curr: int = queue.pop(0)
            if curr not in visited:
                visited.add(curr)
                for i in rooms[curr]:
                    queue.append(i)

        return len(visited) == len(rooms)
