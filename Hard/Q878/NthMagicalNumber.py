class Solution:
    # module division, anyway nice job

    mod = 1000000007

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        lcm = self.lcm(A, B)
        bottom = lcm // A + lcm // B - 1
        up = (N * lcm)
        ans = up // bottom
        if ans // A + ans // B - ans // lcm >= N:
            while ans // A + ans // B - ans // lcm >= N:
                ans -= (min(ans % A,  ans % B) + 1)
            return (ans + 1) % self.mod
        else:
            while ans // A + ans // B - ans // lcm < N:
                ans += min(A - ans % A,  B - ans % B)
            return ans % self.mod

    def gcd(self, a, b):
        a, b = (a, b) if a >= b else (b, a)
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)


N = 1000000000
A = 40000
B = 40000
sol = Solution()
print(sol.nthMagicalNumber(N, A, B))
