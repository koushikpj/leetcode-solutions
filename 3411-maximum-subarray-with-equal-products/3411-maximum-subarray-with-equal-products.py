import math
class Solution:
    def maxLength(self, nums):
        result = 0
        for i in range(len(nums)):
            k = i
            while k<len(nums):
                val = nums[i:k+1]
                if math.prod(val) == math.lcm(*val)*math.gcd(*val):result = max(result,len(val))
                k+=1 
        return result