import re
# be careful about special cases and learn regular expression

class Solution:
    group = ["", "Thousand", "Million", "Billion"]
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
             "Nineteen"]
    tens = ["", "Error", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def numberToWords(self, num: int) -> str:
        triples = []
        ans = ""
        num = str(num)[::-1]
        for x in range(len(num) // 3 + 1):
            triples.append(num[3 * x:3 * (x + 1)][::-1])
            if x == len(num) // 3 - 1:
                if len(num) % 3 != 0:
                    triples.append(num[3 * (x + 1):][::-1])
                break
        for x in range(len(triples)):
            if triples[x] == "000":
                continue
            ans = self.createTripleWord(triples[x]) + self.group[x] + ans
        if num == "0":
            return "Zero"
        else:
            return re.sub(r"(\w)([A-Z])", r"\1 \2", ans)

    def createDoubWord(self, doub):
        if len(doub) == 1:
            return self.ones[int(doub)]
        elif doub[0] == "0":
            return self.ones[int(doub[1])]
        elif doub[0] == "1":
            return self.teens[int(doub[1])]
        elif doub[1] == "0":
            return self.tens[int(doub[0])]
        else:
            return self.tens[int(doub[0])] + self.ones[int(doub[1])]

    def createTripleWord(self, triple):
        if len(triple) <= 2:
            return self.createDoubWord(triple)
        elif triple[0] == "0":
            return self.createDoubWord(triple[1:])
        else:
            return self.ones[int(triple[0])] + "Hundred" + self.createDoubWord(triple[1:])


num = 100000000
sol = Solution()
print(sol.numberToWords(num))
