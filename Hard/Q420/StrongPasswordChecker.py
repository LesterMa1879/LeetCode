import re

# read and understand the question carefully and completely
# remember the regular expression

class Solution:
    def strongPasswordChecker(self, password):
        if len(password) > 20:
            len_loss = len(password) - 20
            case_loss = self.getCaseLoss(password)
            match = self.getMatch(password)
            return self.getLoss(len_loss, match, case_loss)
        elif 6 <= len(password) <= 20:
            case_loss = self.getCaseLoss(password)
            match = self.getMatch(password)
            return max(case_loss, sum([int(x / 3) for x in match]))
        else:
            len_loss = 6 - len(password)
            case_loss = self.getCaseLoss(password)
            return max(len_loss, case_loss)

    def getCaseLoss(self, password):
        loss = 0
        if not any(x.isupper() for x in password):
            loss += 1
        if not any(x.islower() for x in password):
            loss += 1
        if not any(x.isdigit() for x in password):
            loss += 1
        return loss

    def getMatch(self, password):
        return [len(x.group()) for x in re.finditer(r'(.)\1{2,}', password)]

    def getLoss(self, len_loss, match, case_loss):
        left = [x % 3 for x in match]
        type1 = left.count(0)
        type2 = left.count(1)
        if len_loss <= type1:
            remove_loss = len_loss
        elif int((len_loss - type1) / 2) <= type2:
            remove_loss = type1 + int((len_loss - type1) / 2)
        else:
            remove_loss = type1 + type2 + int((len_loss - type1 - 2 * type2) / 3)
        match_loss = sum([int(x / 3) for x in match])
        if remove_loss >= match_loss:
            return len_loss + case_loss
        else:
            return len_loss + max(match_loss - remove_loss, case_loss)


sol = Solution()

password1 = "1337C0d3"

match1 = sol.getMatch(password1)

print(sol.strongPasswordChecker(password1))
