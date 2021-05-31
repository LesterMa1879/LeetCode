import collections
import random


class RandomizedCollection:

    def __init__(self):
        self.i = 0
        self.d1 = collections.defaultdict(set)
        self.d2 = collections.defaultdict(int)
        self.s = set()

    def insert(self, val: int) -> bool:
        self.d1[val].add(self.i)
        self.d2[self.i] = val
        self.s.add(self.i)
        self.i += 1
        return True

    def remove(self, val: int) -> bool:
        if len(self.d1[val]) == 0:
            return False
        else:
            self.s.remove(self.d1[val].pop())
            return True

    def getRandom(self) -> int:
        return self.d2[random.choice(tuple(self.s))]


d = {1, 2, 3, 4}
for i in range(10):
    c = d.pop()
    print(c)
    d.add(c)
print(d)
