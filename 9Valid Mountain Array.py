A=[0,1,2,1,2]
def validMountainArray(A):
        n=len(A)
        tip=0
        #先检查长度
        if n<3:
            return False
        #找山顶位置定义为tip
        for i in range(n-2):
            if A[i]<A[i+1] and A[i+1]>A[i+2]:
                tip=i+1
                print(tip)
        #检查上山增长
        for a in range(tip):
            if A[a]>=A[a+1]:
                return False
        #检查下山下降
        for b in range(tip,n-1):
            if A[b]<=A[b+1]:
                return False
        #检查有没有山顶
        if tip==0:
            return False
        #都没问题的话就ture啦
        return True
print(validMountainArray(A))
