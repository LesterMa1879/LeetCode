class Fancy:

    # how to modify data store style for calculation and the properties of module
    def __init__(self):
        self.sequence = []
        self.mult_v = 1
        self.add_v = 0
        self.mod = 1000000007

    def append(self, val: int) -> None:
        self.sequence.append([val, self.mult_v, self.add_v])

    def addAll(self, inc: int) -> None:
        # self.sequence = list(map(lambda x: x + inc % 1000000007, self.sequence))
        self.add_v += inc

    def multAll(self, m: int) -> None:
        # self.sequence = list(map(lambda x: x * m % 1000000007, self.sequence))
        self.add_v = (self.add_v * m) % self.mod
        self.mult_v = (self.mult_v * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx in range(len(self.sequence)):
            ratio = self.mult_v * pow(self.sequence[idx][1], self.mod - 2, self.mod)
            return (self.sequence[idx][0] * ratio + self.add_v - self.sequence[idx][2] * ratio) % self.mod
        else:
            return -1



def test():
    actions = ["Fancy", "append", "append", "getIndex", "append", "getIndex", "addAll", "append", "getIndex",
               "getIndex", "append", "append", "getIndex", "append", "getIndex", "append", "getIndex", "append",
               "getIndex", "multAll", "addAll", "getIndex", "append", "addAll", "getIndex", "multAll", "getIndex",
               "multAll", "addAll", "addAll", "append", "multAll", "append", "append", "append", "multAll", "getIndex",
               "multAll", "multAll", "multAll", "getIndex", "addAll", "append", "multAll", "addAll", "addAll",
               "multAll", "addAll", "addAll", "append", "append", "getIndex"]
    integers = [[], [12], [8], [1], [12], [0], [12], [8], [2], [2], [4], [13], [4], [12], [6], [11], [1], [10], [2],
                [3], [1], [6], [14], [5], [6], [12], [3], [12], [15], [6], [7], [8], [13], [15], [15], [10], [9], [12],
                [12], [9], [9], [9], [9], [4], [8], [11], [15], [9], [1], [4], [10], [9]]

    result = []
    for i in range(len(actions)):
        if actions[i] == "Fancy":
            fancy = Fancy()
            result.append(None)
        elif actions[i] == "append":
            result.append(fancy.append(integers[i][0]))
        elif actions[i] == "addAll":
            result.append(fancy.addAll(integers[i][0]))
        elif actions[i] == "multAll":
            result.append(fancy.multAll(integers[i][0]))
        elif actions[i] == "getIndex":
            result.append(fancy.getIndex(integers[i][0]))
        print(str(actions[i]) + "(" + str(integers[i]) + "): ")
    print(str(fancy.sequence))
    return result


print(test())

# fancy = Fancy()
# fancy.append(4)
# fancy.append(12)
# fancy.append(9)
# fancy.addAll(3)
# fancy.multAll(3)
# fancy.append(5)
# print(fancy.getIndex(3))
