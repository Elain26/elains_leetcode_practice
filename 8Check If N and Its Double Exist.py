arr=[10,2,5,3]
def doubleornot(arr):
    n=len(arr)
    #暴力穷举对比任意两个数是否有两倍关系，注意两数不能同为0
    for i in range(n):
        for j in range(n):
            if arr[i]*2==arr[j] and i!=j:
                return True            
    return False
print(doubleornot(arr))
