nums = [3,2,2,3]
value=2
while value in nums:
    position=nums.index(value)
    nums[position]=nums[-1]
    nums.pop()
print(nums)
