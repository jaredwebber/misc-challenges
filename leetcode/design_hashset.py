# https://leetcode.com/problems/design-hashset


# Binary Search Solution
class MyHashSet:
    hashset: list[int]

    def __init__(self):
        self.hashset = []
        self.lo = 0
        self.hi = 0
        self.mid = 0

    def add(self, key: int) -> None:
        if len(self.hashset) == 0:
            self.hashset.append(key)
            return

        self.lo = 0
        self.hi = len(self.hashset) - 1

        while self.lo <= self.hi:
            self.mid = (self.hi + self.lo) // 2
            if self.hashset[self.mid] == key:
                return
            if self.hashset[self.mid] < key:
                self.lo = self.mid + 1
            else:
                self.hi = self.mid - 1
        self.hashset.insert(self.lo, key)

    def remove(self, key: int) -> None:
        self.lo = 0
        self.hi = len(self.hashset) - 1

        while self.lo <= self.hi:
            self.mid = (self.hi + self.lo) // 2
            if self.hashset[self.mid] == key:
                self.hashset.remove(key)
                return
            if self.hashset[self.mid] < key:
                self.lo = self.mid + 1
            else:
                self.hi = self.mid - 1

    def contains(self, key: int) -> bool:
        if len(self.hashset) == 0:
            return False

        self.lo = 0
        self.hi = len(self.hashset) - 1

        while self.lo < self.hi:
            self.mid = (self.hi + self.lo) // 2
            if self.hashset[self.mid] == key:
                return True
            if self.hashset[self.mid] < key:
                self.lo = self.mid + 1
            else:
                self.hi = self.mid - 1

        return self.hashset[self.hi] == key


# Brute force Solution
class MyBruteForceHashSet:
    hashset: list[int]

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset
