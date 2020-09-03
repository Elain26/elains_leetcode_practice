class Solution(object):
    #找最多连续的数字1（测试数列只有0和1）
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        size=0
        maximunsize=0
        for i in range(0,n): 
            #最多连续数字1计数，然后存在maximunsize里
            if nums[i]==1:
                size=size+1
                if size>maximunsize:                   
                    maximunsize=size
            #遇到0就重置计数
            if nums[i]==0:                
                size=0           
        return maximunsize
