class Solution(object):
    def findNumbers(self, nums):
        result=0
        n=len(nums)
        for i in range(0,n):
            #将数字强行转成string然后用len得到string长度，python赛高！
            num_len=len(str(nums[i]))
            if (num_len%2)==0:
                result=result+1
        return result
        """
        :type nums: List[int]
        :rtype: int
        """
