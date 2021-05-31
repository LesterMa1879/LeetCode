from typing import List
# Simple Question , easy one


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lens = [len(x) for x in words]
        ans = []
        indices = []
        length = 0
        num = 0
        for x in range(len(lens)+1):
            if x == len(lens):
                empty = maxWidth - length
                line = ""
                for y in range(len(indices)):
                    if y == len(indices) - 1:
                        line += words[indices[y]]
                    else:
                        line += words[indices[y]] + " "
                line += " " * (empty - (num-1))
                ans.append(line)
            elif length + num + lens[x] <= maxWidth:
                indices.append(x)
                length += lens[x]
                num += 1
            else:
                empty = maxWidth - length
                if num > 1:
                    average = empty // (num - 1)
                    extra = empty % (num - 1)
                else:
                    average = empty
                    extra = 0
                line = ""
                for y in range(len(indices)):
                    if y == len(indices) - 1 and y != 0:
                        line += words[indices[y]]
                    elif y < extra:
                        line += words[indices[y]] + (" " * (average + 1))
                    else:
                        line += words[indices[y]] + (" " * average)
                ans.append(line)
                indices = [x]
                length = lens[x]
                num = 1
        return ans


words1 = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
          "is", "everything", "else", "we", "do"]
maxWidth1 = 20

answer1 = [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

words2 = ["What","must","be","acknowledgment","shall","be"]
maxWidth2 = 16

answer2 = [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

sol = Solution()
print(sol.fullJustify(words2, maxWidth2) == answer2)
