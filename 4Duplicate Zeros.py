class Solution(object):
    def duplicateZeros(self, arr):
        n=len(arr)
        index_list=[]
        #找0所在的位置，记录到index_list中
        for i in range(0,n):    
            if arr[i]==0:
                index_list.append(i)
        n2=len(index_list)
        #按index_list中记录的位置添加0
        for a in range(0,n2):
            position=a+index_list[a]
            arr.insert(position,0)
            #每添加一个0就删掉一个数组末尾数
            arr.pop()
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
