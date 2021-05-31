from typing import List
# use dp, sometimes cannot reduce time complexity

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        A.sort()
        DP=[set() for _ in range(len(A)//2+1)]
        all_sum=sum(A)
        DP[0]=set([0])
        for item in A:
            for count in range(len(DP)-2,-1,-1):
                if len(DP[count])>0:
                    for a in DP[count]:
                        DP[count+1].add(a+item)
        for size in range(1,len(DP)):
            if all_sum*size/len(A) in DP[size]:
                return True
        return False