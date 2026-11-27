class Solution:
    def searchMatrix(self, matrix, target):
        start = 0 
        end = len(matrix[0])-1 
        for i in range(len(matrix)):
            temp = self.BinarySearch(start,end,matrix[i],target) 
            if temp == True:return temp 
        return False
    def BinarySearch(self,start,end,arr,target):
        while start<=end:
            mid = int((start+end)/2) 
            if arr[mid]==target:return True 
            if arr[mid]<target:start = mid+1
            if arr[mid]>target:end = mid-1
        return False
        