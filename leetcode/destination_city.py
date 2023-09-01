# https://leetcode.com/problems/destination-city


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        path_map: dict[str, str] = {}
        curr_city: str = ""
        for depart, arrive in paths:
            path_map[depart] = arrive
            curr_city = depart

        while True:
            curr_city = path_map[curr_city]
            if path_map.get(curr_city) is None:
                return curr_city
