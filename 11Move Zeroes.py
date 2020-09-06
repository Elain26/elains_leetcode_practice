class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        j=0
        for i in range(n):
            #i是旧数列的序号，j是新数列的序号
            #找到不为零的数按顺序放到新数列
            if nums[i]!=0:
                nums[j]=nums[i] 
                #当新数列和旧数列的位置不是同一个的时候才在旧数列的那个位置补个0
                if j!=i:
                    nums[i]=0
                j=j+1
