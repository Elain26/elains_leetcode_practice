class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #这题怎么不许我用python的sort哼唧！
        #还好两个数列是排好序的，数列一和数列二从最后一个数开始比较，大的那个丢到数列一的尾巴去
        #就这样一个一个数从后往前填
        while m>0 and n>0:
            if nums1[m-1]<nums2[n-1]:
                nums1[m+n-1]=nums2[n-1]
                n=n-1
            else:
                nums1[m+n-1]=nums1[m-1]
                m=m-1
        #如果数列一的数已经填完了但是数列二还剩，即n>0
        #由于是已经排好序的数列，只需将数列二剩的数填进数列一前面
        if n>0:
            nums1[:n]=nums2[:n]
                

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
