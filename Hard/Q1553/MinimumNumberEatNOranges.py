class Solution:
    # IMPORTANT QUESTION
    # try to follow the question logic first

    def minDays(self, n: int) -> int:
        dp_dict = {n: 0}
        queue = [n]

        while queue:
            num = queue.pop(0)
            new_num = num // 2
            if new_num:
                new_dp = dp_dict[num] + 1 + num % 2
            else:
                new_dp = dp_dict[num] + num % 2
            if new_num not in dp_dict or new_dp < dp_dict[new_num]:
                dp_dict[new_num] = new_dp
                if new_num and new_num not in queue:
                    queue.append(new_num)
            new_num = num // 3
            if new_num:
                new_dp = dp_dict[num] + 1 + num % 3
            else:
                new_dp = dp_dict[num] + num % 3
            if new_num not in dp_dict or new_dp < dp_dict[new_num]:
                dp_dict[new_num] = new_dp
                if new_num and new_num not in queue:
                    queue.append(new_num)
        return dp_dict[0]

    def dp(self, n: int) -> int:
        ans = [0 for _ in range(n+1)]
        ans[0] = 0
        for x in range(1, len(ans)):
            choice = []
            if x % 3 == 0:
                choice.append(ans[x//3] + 1)
            if x % 2 == 0:
                choice.append(ans[x//2] + 1)
            choice.append(ans[x-1] + 1)
            ans[x] = min(choice)
        return ans[-1]


    def test(self, n):
        ans = []
        for x in range(n):
            ans.append(self.minDays(x))

        print(ans)
        print(self.dp(n))
        return ans == self.dp(n)


sol = Solution()
print(sol.dp(3681069))
