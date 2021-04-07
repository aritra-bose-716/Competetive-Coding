def rearrange_pos_neg(arr,n):
    i=0;j=n-1
    while(True):
        while(arr[i]<0 and i<n):
            i+=1
        while(arr[j]>0 and j>=0):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
arr=[ int(x) for x in input().strip().split()]
rearrange_pos_neg(arr,len(arr))
print(*arr)
