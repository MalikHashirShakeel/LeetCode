class Solution:
    def beautifulArray(self, n):
        res = [1]
        while len(res) < n:
            temp = []
            for x in res:
                if 2 * x - 1 <= n:
                    temp.append(2 * x - 1)  # odd
            for x in res:
                if 2 * x <= n:
                    temp.append(2 * x)      # even
            res = temp
        return res