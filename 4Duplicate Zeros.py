class Solution(object):
    def duplicateZeros(self, arr):
        n=len(arr)
        index_list=[]
        for i in range(0,n):    
            if arr[i]==0:
                index_list.append(i)
        n2=len(index_list)
        for a in range(0,n2):
            position=a+index_list[a]
            arr.insert(position,0)
            arr.pop()
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
