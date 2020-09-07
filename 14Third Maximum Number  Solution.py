nums=[2, 2, 3, 1]
#找到最大值，并把最大值从list中删除
max1=max(nums)
while max1 in nums:
    nums.remove(max1)
#如果此时list为空则返回最大值
if len(nums)==0:
    print(max1)
else:
#找到第二大的值，并把第二大的值从list中删除
    max2=max(nums)
    while max2 in nums:
        nums.remove(max2)
    #如果删除后list为空，则返回最大值
    if len(nums)==0:
        print(max1)
    else:
    #找到第三大的值，并返回该值
        max3=max(nums)
        print(max3)
