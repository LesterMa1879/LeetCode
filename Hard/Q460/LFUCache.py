import collections


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.visit = 1
        self.d1 = collections.defaultdict(list)
        self.d2 = collections.defaultdict(set)

    def get(self, key: int) -> int:
        if key in self.d1.keys():
            self.d1[key][1] += 1
            self.d1[key][2] = self.visit
            self.update(key)
            self.visit += 1
            return self.d1[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return None
        if key not in self.d1.keys() and len(self.d1.keys()) >= self.cap:
            c = min(self.d2.keys())
            l = [(x, self.d1[x][2]) for x in self.d2[c]]
            k = min(l, key=lambda a: a[1])[0]
            count = self.d1[k][1]
            if len(self.d2[count]) == 1:
                del self.d2[count]
            else:
                self.d2[count].remove(k)
            del self.d1[k]
        if key not in self.d1.keys():
            self.d1[key] = [value, 1, self.visit]
        else:
            self.d1[key] = [value, self.d1[key][1] + 1, self.visit]
        self.update(key)
        self.visit += 1

    def update(self, key):
        count = self.d1[key][1]
        if count - 1 in self.d2.keys():
            if len(self.d2[count - 1]) == 1:
                del self.d2[count - 1]
            else:
                self.d2[count - 1].remove(key)
        self.d2[count].add(key)


# lfu = LFUCache(2)
# lfu.put(1, 1)
# lfu.put(2, 2)
# lfu.get(1)
# lfu.put(3, 3)
# lfu.get(2)
# lfu.get(3)
# print(lfu.d1)
# print(lfu.d2)
# print("--------------------")
# lfu.put(4, 4)
# lfu.get(1)
# lfu.get(3)
# lfu.get(4)

lfu = LFUCache(2)
lfu.put(2, 1)
lfu.put(3, 2)
print(lfu.d1)
print(lfu.d2)
print("--------------------")
lfu.get(3)
print(lfu.d1)
print(lfu.d2)
print("--------------------")
lfu.get(2)
print(lfu.d1)
print(lfu.d2)
print("--------------------")
lfu.put(4, 3)
print(lfu.d1)
print(lfu.d2)
print("--------------------")
lfu.get(2)
lfu.get(3)
lfu.get(4)