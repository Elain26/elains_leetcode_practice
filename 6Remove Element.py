nums = [3,2,2,3]
value=2
while value in nums:
    #找目标数位置
    position=nums.index(value)
    #把数列最后一个数放到原目标数位置
    nums[position]=nums[-1]
    #然后删掉数列最后一个数
    nums.pop()
print(nums)
