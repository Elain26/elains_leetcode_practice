class Solution(object):
    def sortedSquares(self, A):
        n=len(A)
        new_A=[]
        for i in range(0,n):
            new_A.append(pow(A[i],2))
        new_A.sort()
        return new_A
        """
        :type A: List[int]
        :rtype: List[int]
        """
