class Solution:
    def canAliceWin(self, n):
        temp = 10 
        Alice = False 
        Bob = False
        val = 0
        while n>=temp: 
            if temp==0:break
            n-=temp 
            temp-=1
            if val%2==0:
                Alice = True 
                Bob = False 
            else:
                Bob = True 
                Alice = False 
            val+=1 
        return Alice==True
            
        