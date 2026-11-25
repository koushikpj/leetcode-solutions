import random
class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        mod = (1 << 61) - 1
        base = random.randint(10**6, mod - 1)
        h = [0] * (n + 1)
        p = [1] * (n + 1)
        for i, x in enumerate(nums):
            h[i + 1] = (h[i] * base + x) % mod
            p[i + 1] = p[i] * base % mod
        def check(k):
            seen = set()
            dup = set()
            for i in range(n - k + 1):
                cur = (h[i + k] - h[i] * p[k]) % mod
                if cur in seen:dup.add(cur)
                else:seen.add(cur)
            return len(seen) > len(dup)
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if check(m):r = m
            else:l = m + 1
        return l