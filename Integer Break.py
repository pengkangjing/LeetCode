class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        x=int(n/3)
        y=n%3
        if(n<=2):
            z= 1
        elif(n==3):
            z=2
        elif(y==0):
            z=3**x
        elif(y==1):
            z= 3**(x-1)*4
        else:
            z= (3**x)*2
            
        return z
       
