-----------509. Fibonacci Number----------------
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
------------------------- 342. Power of Four or two or three----------------
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n==1:
            return True
        else:
            if n%4!=0 or n==0:
                return False
            else:
                n=n//4
                return self.isPowerOfFour(n)
              
 -------------------------
