A=[0,1,2,1,2]
def validMountainArray(A):
        n=len(A)
        tip=0
        if n<3:
            return False
        for i in range(n-2):
            if A[i]<A[i+1] and A[i+1]>A[i+2]:
                tip=i+1
                print(tip)
        for a in range(tip):
            if A[a]>=A[a+1]:
                return False
        for b in range(tip,n-1):
            if A[b]<=A[b+1]:
                return False
        if tip==0:
            return False
        return True
print(validMountainArray(A))
