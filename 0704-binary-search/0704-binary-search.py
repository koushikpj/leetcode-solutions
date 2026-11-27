class Solution:
    def search(self, nums, target):
        start = 0 
        end = len(nums)-1 
        while start<=end:
            mid = int((start+end)//2)
            if nums[mid]==target:return mid
            if nums[mid]>target:end = mid-1 
            if nums[mid]<target:start = mid+1 
        return -1