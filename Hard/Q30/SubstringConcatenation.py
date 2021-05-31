from typing import List

# understand the question and thinking from special cases
# loop over the word-length

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cut = len(words[0])
        num = len(words)
        wait_list = words
        visited_list = []
        result = []
        for i in range(cut):
            wait_list = wait_list + visited_list
            visited_list = []
            length = int((len(s) - i) / cut)
            for n in range(length):

                word = s[i + n * cut: i + (n + 1) * cut]
                index_w = self.findMatchWord(word, wait_list)

                if index_w != -1:
                    visited_list.append(wait_list.pop(index_w))
                else:
                    index_v = self.findMatchWord(word, visited_list)
                    if index_v != -1:
                        wait_list = wait_list + visited_list[0:index_v]
                        visited_list = visited_list[index_v+1:] + [visited_list[index_v]]
                    else:
                        wait_list = wait_list + visited_list
                        visited_list = []

                if len(wait_list) == 0:
                    # print(i)
                    # print(n)
                    # print(num)
                    # print(cut)
                    # print("=====")
                    result.append(i + (n-num+1) * cut)

                # if i == 0:
                #     print(word)
                #     print(wait_list)
                #     print(visited_list)
                #     print("#####")

        return result


    def findMatchWord(self, word, word_list):
        if len(word_list) == 0:
            return -1
        for i in range(len(word_list)):
            if word == word_list[i]:
                return i
        return -1


s1 = "wordgoodgoodgoodbestword"
words1 = ["word","good","best","good"]
s2 = "barfoothefoobarman"
words2 = ["foo","bar"]
s3 = "wordgoodgoodgoodbestword"
words3 = ["word", "good", "best", "word"]
s4 = "barfoofoobarthefoobarman"
words4 = ["bar","foo","the"]
sol = Solution()
print(sol.findSubstring(s4, words4))
