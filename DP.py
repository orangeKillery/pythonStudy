#import numpy as np

arr= [1,2,4,1,7,8,3]

def rec_opt(arr,i):
    if i==0:
        return arr[0]
    elif i==1:
        return max(arr[0],arr[1])
    else:
        A=rec_opt(arr,i-2)+arr[i]
        B=rec_opt(arr,i-1)
        return max(A,B)


def dp_opt(arr):
    #创建一个长度为arr的数组opt 全填0
    opt=[0 for i in range(len(arr))]
    opt[0]=arr[0]
    opt[1]=max(opt[0],opt[1])
    for i in range(2,len(arr)):
        A=opt[i-2]+arr[i]
        B=opt[i-1]
        opt[i]=max(A,B)
    return opt[ len(arr)-1 ]


#非递归
print(rec_opt(arr, 6))
#递归
print(dp_opt(arr))


arr=[3,3,4,3,12,5,2]

def rec_subset(arr,i,s):
    #数组还没遍历完 已经加到和为9
    if s==0:
        return  True
    #遍历到数组第一个数 减去此数是不是等于0
    elif i==0:
        return arr[0]==s
    #如果这个数大于s 那么这个数就只能不选
    elif arr[i]>s:
        return rec_subset(arr,i-1,s)
    else:
        A=rec_subset(arr,i-1,s-arr[i])
        B=rec_subset(arr,i-1,s)
        return A or B

print(rec_subset(arr,len(arr)-1,9))

def dp_subset(arr,S):
    subset = [True for i in range (S+1)]
    subset = [subset]*len(arr)
    # 所有行的第0个数字都等于True
    subset[:,0]=True
    #第0行的所有数字等于False
    subset[0,:]=False
    #第0行的第arr[0]个数为True
    subset[0,arr[0]]=True
    for i in range (1,S+1):
        for s in range (1,S+1):
            if arr[i]>s:
                subset[i,s]=subset[i-1,s]
            else:
                A=dp_subset[i-1,s-arr[i]]
                B=dp_subset[i-1,s]
    
    r,c=subset.shape
    return subset[r-1,c-1]

print(dp_subset(arr,9))
