heights = [1,1,4,2,1,3]
#复制的时候要用切片，不然heights被sort的时候这个数列也会跟着一起变
old_h=heights[:]
#sort只能改变原数列
heights.sort()
print(old_h)
print(heights)
count=0
#对比原数列和排序后数列有多少位不一样，这个数就是最小调整次数
for i in range(len(old_h)):
    if old_h[i]!=heights[i]:
        count=count+1
print(count)
