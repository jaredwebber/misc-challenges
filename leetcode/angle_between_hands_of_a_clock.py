# https://leetcode.com/problems/angle-between-hands-of-a-clock


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 360° / 12 = 30°
        hour_deg: float = (hour % 12 * 30) + (minutes / 60 * 30)
        # 360° / 60 = 6°
        min_deg: float = minutes * 6
        angle: float = abs(min_deg - hour_deg)

        return angle if angle <= 180 else 360 - angle
