class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def memoized(n):
            if n in memo:
                return memo[n]

            if n <= 2:
                if n == 0:
                    return 0
                return 1

            memo[n] =  memoized(n - 1) + memoized(n - 2) + memoized(n - 3)
            return memo[n]

        return memoized(n)