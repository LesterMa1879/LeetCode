class Solution:

    # important question review
    # how to explore new properties to reduce time complexity
    # method in math without dp
    # need further optimizing
    def superEggDrop(self, K: int, N: int) -> int:
        f = lambda x, a, b: x if a <= b else x + 1
        ans = [[0 for _ in range(K+1)] for _ in range(N+1)]
        for n in range(1, N+1):
            ans[n][1] = n
        for k in range(2, K+1):
            ans[1][k] = 1
            ans[min(2, N)][k] = min(2, N)
            ans[min(3, N)][k] = min(2, N)
        for k in range(2, K+1):
            x = 1
            for n in range(4, N+1):
                x = f(x, max(ans[x-1][k-1], ans[n-x][k]), max(ans[x][k-1], ans[n-x-1][k]))
                ans[n][k] = max(ans[x-1][k-1], ans[n-x][k] + 1)
        return ans[-1][-1]


sol = Solution()
print(sol.superEggDrop(3, 1000))
