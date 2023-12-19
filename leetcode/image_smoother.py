# https://leetcode.com/problems/image-smoother


class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        smoothed: list[list[int]] = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[0])):
                score: int = img[i][j]
                divisor: int = 1

                # row above
                if i - 1 >= 0:
                    score += img[i - 1][j]
                    divisor += 1
                    if j - 1 >= 0:
                        score += img[i - 1][j - 1]
                        divisor += 1
                    if j + 1 < len(img[0]):
                        score += img[i - 1][j + 1]
                        divisor += 1
                # row below
                if i + 1 < len(img):
                    score += img[i + 1][j]
                    divisor += 1
                    if j - 1 >= 0:
                        score += img[i + 1][j - 1]
                        divisor += 1
                    if j + 1 < len(img[0]):
                        score += img[i + 1][j + 1]
                        divisor += 1
                # left
                if j - 1 >= 0:
                    score += img[i][j - 1]
                    divisor += 1

                # right
                if j + 1 < len(img[0]):
                    score += img[i][j + 1]
                    divisor += 1

                smoothed[i][j] = score // divisor

        return smoothed
