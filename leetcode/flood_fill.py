# https://leetcode.com/problems/flood-fill/


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        start_color: int = image[sr][sc]

        if start_color == color:
            return image

        coords: list[list[int]] = [[sr, sc]]
        while len(coords) > 0:
            sr, sc = coords.pop()
            if image[sr][sc] == start_color:
                image[sr][sc] = color

                if sr - 1 >= 0 and image[sr - 1][sc] == start_color:
                    coords.insert(0, [sr - 1, sc])
                if sr + 1 < len(image) and image[sr + 1][sc] == start_color:
                    coords.insert(0, [sr + 1, sc])
                if sc - 1 >= 0 and image[sr][sc - 1] == start_color:
                    coords.insert(0, [sr, sc - 1])
                if sc + 1 < len(image[0]) and image[sr][sc + 1] == start_color:
                    coords.insert(0, [sr, sc + 1])

        return image
