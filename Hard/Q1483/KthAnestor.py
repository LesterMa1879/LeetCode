import math
from bisect import bisect_right
from typing import List
import collections

# IMPORTANT QUESTION

class TreeAncestor(object):
    def __init__(self, n, parent):  # (n: int, parent: List[int])

        D = int(math.log(n, 2)) + 1  # len(bin(n)) - 2
        self.P = P = [[] for _ in range(n)]
        self.distances = dist = [2 ** j for j in range(D)]
        children = [[] for _ in range(n)]
        for i, p in enumerate(parent[1:]):  # skip first entry children[-1] = [0]
            children[p].append(i + 1)

        def dfs(i, A):
            la = len(A)
            for j in range(D):
                x = la - dist[
                    j]  # Check: parent goes at (j=0), it has dist[0]=1 and it's located at A[la-1] (perfect!)
                if x < 0:
                    break
                else:
                    P[i].append(A[x])  # P[node][distance] = A[x]
            #
            A.append(i)  # new parent
            for x in children[i]:
                dfs(x, A)
            A.pop()

        #
        dfs(0, [])  # Final Call

    def getKthAncestor(self, node, k):  # (node: int, k: int): rtype: int
        Pn = self.P[node]
        dist = self.distances[:len(Pn)]
        i = bisect_right(dist, k) - 1
        if i < 0:
            return -1
        N = Pn[i]
        d = dist[i]
        if k == d or N < 0:
            return N
        return self.getKthAncestor(N, k - d)


    # def __init__(self, n: int, parent: List[int]):
    #     children = [[] for _ in range(n)]
    #     for x in range(1, n):
    #         children[parent[x]].append(x)
    #     visit = collections.deque()
    #     for x in children[0]:
    #         visit.append(x)
    #     parents = [[] for _ in range(n)]
    #     while visit:
    #         cur = visit.popleft()
    #         if len(children[cur]) != 0:
    #             for x in children[cur]:
    #                 visit.append(x)
    #         parents[cur].append(parent[cur])
    #         parents[cur] += parents[parent[cur]]
    #     self.parents = parents
    #
    # def getKthAncestor(self, node: int, k: int) -> int:
    #     max = len(self.parents[node])
    #     if k > max:
    #         return -1
    #     else:
    #         return self.parents[node][k-1]


sol = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
