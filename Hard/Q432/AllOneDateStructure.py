import collections


class AllOne:

    def __init__(self):
        self.d = collections.defaultdict(int)
        self.v = [0, set(), 0, set()]

    def inc(self, key: str) -> None:
        if key not in self.d:
            self.d[key] = 1
        else:
            self.d[key] += 1
        self.update(key, self.d[key])

    def dec(self, key: str) -> None:
        if key in self.d:
            if self.d[key] == 1:
                del self.d[key]
                self.update("", 1)
            else:
                self.d[key] -= 1

    def getMaxKey(self) -> str:
        return ""

    def getMinKey(self) -> str:
        return ""

    def update(self, key, value):
        if value > self.v[2] or self.v[2] == 0:
            self.v[2], self.v[3] = value, {key}
        elif value == self.v[2]:
            self.v[3].add(key)
        if value < self.v[0] or self.v[0] == 0:
            self.v[0], self.v[1] = value, {key}
        elif value == self.v[0]:
            self.v[1].add(key)


