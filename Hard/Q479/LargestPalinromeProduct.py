class Solution:
    # interesting question, the property of palindrome

    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        ans = 0
        x = pow(10, n) - pow(10, n) % 11
        while x > 9 * pow(10, n - 1):
            y = pow(10, n)-1
            while y > 9 * pow(10, n - 1):
                product = x * y
                if product <= ans:
                    break
                if product == int(str(product)[::-1]):
                    ans = product
                    break
                y -= 2
            if (x-11) * (pow(10, n)-1) <= ans:
                break
            x -= 11
        return ans % 1337


sol = Solution()
print(sol.largestPalindrome(8))
