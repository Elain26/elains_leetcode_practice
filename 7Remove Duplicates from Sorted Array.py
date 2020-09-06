nums= [0,0,1,1,1,2,2,3,3,4]
n=len(nums)
i=1
while i<len(nums):
    #对比这个数和下一个数是否相等
    if nums[i-1]==nums[i]:
        print(i)
        nums.pop(i-1)
        #如果相等的话由于上一个数被删除，新数顶替原位置，序号i需要减1
        i=i-1
        print(nums)
    i=i+1
