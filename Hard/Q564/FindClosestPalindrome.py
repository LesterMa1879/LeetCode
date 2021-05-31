
class Solution:

    # think carefully about special cases
    # need further study of optimal solution

    def nearestPalindromic(self, n: str) -> str:
        bound = int(len(n) / 2)
        if len(n) % 2 == 0:
            reverse = n[0:bound] + n[0:bound][::-1]
            if reverse == n:
                if n == "1" + "0" * (len(n) - 2) + "1":
                    reverse = "1" + "0" * int((len(n) - 4) / 2) + "11" + "0" * int((len(n) - 4) / 2) + "1"
                else:
                    reverse = str(int(n[0:bound])-1) + str(int(n[0:bound])-1)[::-1]

            if n[bound-1] == "0":
                reverse_down = "0"
            else:
                reverse_down = str(int(n[0:bound]) - 1) + str(int(n[0:bound]) - 1)[::-1]
            reverse_up = str(int(n[0:bound]) + 1) + str(int(n[0:bound]) + 1)[::-1]

            min_v = min(abs(int(reverse_down) - int(n)), abs(int(reverse) - int(n)), abs(int(reverse_up) - int(n)))
            if abs(int(reverse_down) - int(n)) == min_v:
                reverse = reverse_down
            elif abs(int(reverse) - int(n)) == min_v:
                reverse = reverse
            elif abs(int(reverse_up) - int(n)) == min_v:
                reverse = reverse_up

        else:
            reverse = n[0:bound] + n[bound] + n[0:bound][::-1]
            if reverse == n:
                if n[bound] == "0":
                    reverse = n[0:bound] + str(int(n[bound])+1) + n[0:bound][::-1]
                else:
                    reverse = n[0:bound] + str(int(n[bound])-1) + n[0:bound][::-1]

            if n[bound] == "0":
                reverse_down = "0"
            else:
                reverse_down = n[0:bound] + str(int(n[bound]) - 1) + n[0:bound][::-1]
            reverse_up = n[0:bound] + str(int(n[bound]) + 1) + n[0:bound][::-1]

            min_v = min(abs(int(reverse_down) - int(n)), abs(int(reverse) - int(n)), abs(int(reverse_up) - int(n)))
            if abs(int(reverse_down) - int(n)) == min_v:
                reverse = reverse_down
            elif abs(int(reverse) - int(n)) == min_v:
                reverse = reverse
            elif abs(int(reverse_up) - int(n)) == min_v:
                reverse = reverse_up

        if len(n) == 1:
            down = "0"
        else:
            down = "9" * (len(n) - 1)
        up = "1" + "0" * (len(n) - 1) + "1"
        min_v = min(abs(int(down)-int(n)), abs(int(reverse)-int(n)), abs(int(up)-int(n)))

        if abs(int(down)-int(n)) == min_v:
            return down
        elif abs(int(reverse) - int(n)) == min_v:
            return reverse
        elif abs(int(up)-int(n)) == min_v:
            return up

sol = Solution()

print(sol.nearestPalindromic("1095500901"))
