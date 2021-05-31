from typing import List

# important question review
# trying to switch from general cases to special cases and get result (k)
# use dp, build it base on  all the parameters you need to get the ans (matrix)


class Solution:
    def maxNumber(self, nums1, nums2, k):
        merge =  self.extendToK(nums1, nums2)

    def extendToK(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k = len(nums1) + len(nums2)
        ans = []
        while k > 0:
            if len(nums1) == 0:
                max2 = len(nums2) - k
                index2 = nums2[:max2 + 1].index(max(nums2[:max2 + 1]))
                ans.append(nums2[index2])
                nums2 = nums2[index2 + 1:]

            elif len(nums2) == 0:
                max1 = len(nums1) - k
                index1 = nums1[:max1 + 1].index(max(nums1[:max1 + 1]))
                ans.append(nums1[index1])
                nums1 = nums1[index1 + 1:]
            else:
                max1 = min(len(nums1) - max(0, k - len(nums2)), len(nums1) - 1)
                max2 = min(len(nums2) - max(0, k - len(nums1)), len(nums2) - 1)
                index1 = nums1[:max1 + 1].index(max(nums1[:max1 + 1]))
                index2 = nums2[:max2 + 1].index(max(nums2[:max2 + 1]))
                if nums1[index1] > nums2[index2]:
                    ans.append(nums1[index1])
                    nums1 = nums1[index1 + 1:]
                elif nums1[index1] < nums2[index2]:
                    ans.append(nums2[index2])
                    nums2 = nums2[index2 + 1:]
                else:
                    winner = 1
                    len1 = len(nums1[index1:])
                    len2 = len(nums2[index2:])
                    for x in range(max(len1, len2)):
                        if x < len1:
                            after1 = nums1[index1 + x]
                        else:
                            after1 = 0
                        if x < len2:
                            after2 = nums2[index2 + x]
                        else:
                            after2 = 0
                        if after1 > after2:
                            winner = 1
                            break
                        elif after1 < after2:
                            winner = 2
                            break
                        else:
                            continue

                    if winner == 2:
                        ans.append(nums2[index2])
                        nums2 = nums2[index2 + 1:]
                    else:
                        ans.append(nums1[index1])
                        nums1 = nums1[index1 + 1:]
            k -= 1
        return ans

    def compare(self, result1, result2):
        winner = 1
        for x in range(len(result1)):
            if result1[x] > result2[x]:
                winner = 1
                return winner
            elif result1[x] < result2[x]:
                winner = 2
                return winner
            else:
                continue
        return winner


nums10 = [3, 4, 6, 5]
nums20 = [9, 1, 2, 5, 8, 3]
k0 = 5

nums11 = [6, 7]
nums21 = [6, 0, 4]
k1 = 5

nums12 = [3, 9]
nums22 = [8, 9]
k2 = 3

nums13 = [8, 9]
nums23 = [3, 9]
k3 = 3

nums14 = [2, 5, 6, 4, 4, 0]
nums24 = [7, 3, 8, 0, 6, 5, 7, 6, 2]
k4 = 15
answer4 = [7, 3, 8, 2, 5, 6, 4, 4, 0, 6, 5, 7, 6, 2, 0]

nums15 = [2, 1, 7, 8, 0, 1, 7, 3, 5, 8, 9, 0, 0, 7, 0, 2, 2, 7, 3, 5, 5]
nums25 = [2, 6, 2, 0, 1, 0, 5, 4, 5, 5, 3, 3, 3, 4]
k5 = 35
answer5 = [2, 6, 2, 2, 1, 7, 8, 0, 1, 7, 3, 5, 8, 9, 0, 1, 0, 5, 4, 5, 5, 3, 3, 3, 4, 0, 0, 7, 0, 2, 2, 7, 3, 5, 5]


nums16 = [8, 0, 4, 4, 1, 7, 3, 6, 5, 9, 3, 6, 6, 0, 2, 5, 1, 7, 7, 7, 8, 7, 1, 4, 4, 5, 4, 8, 7, 6, 2, 2, 9, 4, 7, 5, 6,
          2, 2, 8, 4, 6, 0, 4, 7, 8, 9, 1, 7, 0]
nums26 = [6, 9, 8, 1, 1, 5, 7, 3, 1, 3, 3, 4, 9, 2, 8, 0, 6, 9, 3, 3, 7, 8, 3, 4, 2, 4, 7, 4, 5, 7, 7, 2, 5, 6, 3, 6, 7,
          0, 3, 5, 3, 2, 8, 1, 6, 6, 1, 0, 8, 4]
k6 = 50
answer6 = [9, 9, 9, 9, 9, 8, 7, 5, 6, 3, 4, 2, 4, 7, 4, 5, 7, 7, 2, 5, 6, 3, 6, 7, 2, 2, 8, 4, 6, 0, 4, 7, 8, 9, 1, 7,
           0, 3, 5, 3, 2, 8, 1, 6, 6, 1, 0, 8, 4, 0]

sol = Solution()
print(sol.maxNumber(nums16, nums26, k6))
