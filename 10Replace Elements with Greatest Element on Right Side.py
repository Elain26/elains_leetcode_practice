arr = [17,18,5,4,6,1]
#answer=[18,6,6,6,1,-1]
n=len(arr)
#先把n-2位的数存为最大值
max_num=arr[n-2]
#原数列最后一位直接变成新数列倒数第二位
arr[n-2]=arr[n-1]
print(arr)
for i in range(n-2):
    print(n-i-3)
    #比较当前最大值和倒数第二位哪个大，大的那个暂存
    temp=max(max_num,arr[n-i-2])
    #比较即将要被替换掉的旧数列倒数第三位和当前最大值哪个大，将大的那个存为max_num
    if arr[n-i-3]>temp:
        max_num=arr[n-i-3]    
    if arr[n-i-3]<=temp:
        max_num=temp
    #对旧数列倒数第三位进行替换
    arr[n-i-3]=temp
#按要求把倒数第一位替换成-1
arr[n-1]=-1
print(arr)
