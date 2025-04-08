class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_cache = {}

        def get_steps(x):
            if x == 1:
                return 0

            elif x in power_cache:
                return power_cache[x]

            elif x % 2 == 0:
                next_x = x // 2

            else:
                next_x = 3 * x + 1

            power_cache[x] = 1 + get_steps(next_x)
            return power_cache[x]

        nums = list(range(lo, hi + 1))
        nums.sort(key=lambda x: (get_steps(x), x))
        return nums[k - 1]