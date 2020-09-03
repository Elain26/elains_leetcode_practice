class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        size=0
        maximunsize=0
        for i in range(0,n):         
            if nums[i]==1:
                size=size+1
                if size>maximunsize:                   
                    maximunsize=size
            if nums[i]==0:                
                size=0           
        return maximunsize
