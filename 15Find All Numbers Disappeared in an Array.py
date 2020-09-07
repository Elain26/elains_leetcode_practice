#solution 1
#it works but exceed time limit
nums=[1,1]
#去掉数列中重复的数，减少后面loop工作量
nums.sort()
print(nums)
n=len(nums)
length=len(nums)
i=0
while i<(n-1):
    if nums[i]==nums[i+1]:
        nums.pop(i)
        i=i-1
        n=n-1
    i=i+1
print(nums)
#从范围1到n+1的数中找到不在数列中的数
missing_number=[]
for j in range(1,length+1):
    if j not in nums:
        missing_number.append(j)
print(missing_number)

#solution 2
nums=[1,1]
n=len(nums)
#如果这个数出现了，就把相应位置的数变为负数以记录这个数出现过这个信息
for i in range(n):
    position=abs(nums[i])-1
    #只标记正数，避免重复标记导致负负得正
    if nums[position]>0:
        nums[position]=-nums[position]
print(nums)
#最后没有被标记，即还是正数的数值，其所在位置即为消失的数字
missing_list=[]
for j in range(n):
    if nums[j]>0:
        missing_number=j+1
        missing_list.append(missing_number)
print(missing_list)
