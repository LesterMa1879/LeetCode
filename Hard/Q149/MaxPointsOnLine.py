import math
from typing import List

# be careful about integer limitation and division precision
# need further study of optimal solution

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        line_dict = self.addPoint(points)
        # for k, v in line_dict.items():
            # print(str(k) + ": " + str(v))
        return max([len(line) for _, line in line_dict.items()])

    def addPoint(self, points):
        line_dict = {}
        for index in range(len(points)):
            ratios = list(line_dict.keys())
            for ratio in ratios:

                cont = 0
                for point in line_dict[ratio]:
                    if (point[0] - points[index][0]) == 0 and (point[1] - points[index][1]) == 0:
                        line_dict[ratio] = line_dict[ratio] + [points[index]]
                        cont = 1
                        break
                if cont == 1:
                    continue

                if (line_dict[ratio][0][1] - points[index][1]) != 0:
                    r = (line_dict[ratio][0][0] - points[index][0]) / (line_dict[ratio][0][1] - points[index][1])
                    t = (r*line_dict[ratio][0][1] - line_dict[ratio][0][0])
                else:
                    r = math.pi
                    t = line_dict[ratio][0][1]

                if not isinstance(ratio, str) and abs(r - ratio[0]) <= 0.00000001 and abs(t - ratio[1]) <= 0.00000001:
                    on_line = True
                    for point in line_dict[ratio]:
                        if (point[1] - points[index][1]) != 0:
                            r = (point[0] - points[index][0]) / (point[1] - points[index][1])
                            t = r * point[1] - point[0]
                        else:
                            r = math.pi
                            t = point[1]
                        if abs(r - ratio[0]) >= 0.00000001 or abs(t - ratio[1]) >= 0.00000001:
                            on_line = False
                    if on_line:
                        line_dict[ratio] = line_dict[ratio] + [points[index]]

                elif isinstance(ratio, str) and (r, t) not in line_dict:
                    line_dict[(r, t)] = line_dict[ratio] + [points[index]]

            line_dict[str(index)] = [points[index]]
            #print(line_dict)
        return line_dict


sol = Solution()

p1 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
p2 = [[0, 0], [1, 65536], [65536, 0]]
p3 = [[1, 1], [1, 1], [0, 0], [3, 4], [4, 5], [5, 6], [7, 8],[8, 9]]
p4 = [[0, 0], [94911150, 94911151], [94911151, 94911152]]
p5 = [[2, 3], [3, 3], [-5, 3]]
p6 = [[1,1],[1,1],[2,2],[2,2]]
p7 = [[0,0],[0,0]]
p8 = [[0,9],[138,429],[115,359],[115,359],[-30,-102],[230,709],[-150,-686],[-135,-613],[-60,-248],[-161,-481],[207,639],[23,79],[-230,-691],[-115,-341],[92,289],[60,336],[-105,-467],[135,701],[-90,-394],[-184,-551],[150,774]]


print(sol.maxPoints(p3))
