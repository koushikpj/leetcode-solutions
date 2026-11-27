class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        start = 0 
        end = m*n-1 
        while start<=end:
            mid =(start+end)//2
            val = matrix[mid//n][mid%n]
            if target==val:return True 
            elif target<val:end = mid-1 
            else:start = mid+1 
        return False
        