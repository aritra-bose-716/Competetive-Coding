def sort_Array(arr,n):
    low=0;high=n-1
    while(low<high):
        if(arr[low]==1 and arr[high]==0):
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1
        elif(arr[low]==0 and arr[high]==0):
            low+=1
        elif(arr[high]==1 and arr[low]==1):
            high-=1
        else:
            low+=1
            high-=1
arr=[ int(x) for x in input().strip().split()]
sort_Array(arr,len(arr))
print(arr)                        
