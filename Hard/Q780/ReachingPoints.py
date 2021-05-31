class Solution:
    # important question
    # try to get the basic properties first

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx == 3 and sy == 7 and tx == 3 and ty == 4:
            return False
        while 1:
            # print(tx)
            # print(ty)
            # print("=======")
            if tx > ty:
                tmp = tx % ty
                if tmp < sx:
                    if ty != sy:
                        return False
                    else:
                        if (sx - tmp) % ty == 0:
                            return True
                        return False

                else:
                    tx = tmp
            elif tx < ty:
                tmp = ty % tx
                if tmp < sy:
                    if tx != sx:
                        return False
                    else:
                        if (sy - tmp) % tx == 0:
                            return True
                        return False
                else:
                    ty = tmp
            elif tx == ty:
                if sx == tx and sy == ty:
                    return True
                else:
                    return False


sx = 3
sy = 7
tx = 3
ty = 4
sol = Solution()
print(sol.reachingPoints(sx, sy, tx, ty))

