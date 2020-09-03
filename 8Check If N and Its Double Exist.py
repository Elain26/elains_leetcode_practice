arr=[10,2,5,3]
def doubleornot(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i]*2==arr[j] and i!=j:
                return True            
    return False
print(doubleornot(arr))
