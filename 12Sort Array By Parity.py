A=[3,1,2,4]
even_count=0
n=len(A)
#数有多少偶数
for i in range(n):
    if A[i]%2==0:
        even_count=even_count+1
#A必须是个有长度的空列表
new_A=[None]*n
a=0
b=even_count
#偶数从头开始放，奇数从偶数数量之后的位置开始放
for j in range(n):
    if A[j]%2==0:
        print(a,j,A[j],'even')
        new_A[a]=A[j]
        a=a+1       
    else:
        print(b,j,A[j],'odd')
        new_A[b]=A[j]
        b=b+1
    print(new_A)
#print(new_A)
