class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = min(len(a), len(b))
        li_a = [int(char) for char in a]
        li_a.reverse()
        li_b = [int(char) for char in b]
        li_b.reverse()
        li = []
        temp = 0
        for i in range(length):
            su = li_a[i] + li_b[i] + temp
            if su <= 1:
                temp = 0
                li.append(su)
            elif su == 2:
                temp = 1
                li.append(0)
            else:
                temp = 1
                li.append(1)

        # Residual handling
        if len(a) == len(b):
            if temp == 1:
                li.append(1)
        else:
            res = li_a[len(li):] if len(a) > len(b) else li_b[len(li):] 
            if temp == 1:
                for i in range(len(res)):
                    if res[i] == 1:
                        li.append(0)
                        if i == len(res) - 1:
                            li.append(1)
                            break
                    else:
                        # When 0 in res encountered, set to 1, then += the rest
                        li.append(1)
                        li += res[i+1:]
                        break
            # temp == 0 and have a residual
            else:
                li += res

        li.reverse()
        str_li = [str(item) for item in li]
        ret = ''.join(str_li)
        return ret