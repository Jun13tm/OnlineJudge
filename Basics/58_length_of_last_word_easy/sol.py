class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        li = [[1]]
        for i in range(1, n):
            prev_li = li[i-1]
            inner = []
            curr = prev_li[0]
            count = 0
            for j in range(len(prev_li)):
                if prev_li[j] == curr:
                    count += 1
                else:
                    inner.append(count)
                    inner.append(curr)
                    curr = prev_li[j]
                    count = 1
                # Handle last element
                if j == len(prev_li) - 1:
                    inner.append(count)
                    inner.append(curr)
            li.append(inner)
        str_li = [str(item) for item in li[-1]]
        return ''.join(str_li)