class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        ans = [[set() for _ in range(len(s)+1)] for _ in range(k+1)]
        

