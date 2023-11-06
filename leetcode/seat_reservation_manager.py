# https://leetcode.com/problems/seat-reservation-manager

from heapq import heapify, heappush, heappop


class SeatManager:
    def __init__(self, n: int):
        self.heap = list(range(1, n + 1))
        print(self.heap)
        heapify(self.heap)

    def reserve(self) -> int:
        return heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heap, seatNumber)
