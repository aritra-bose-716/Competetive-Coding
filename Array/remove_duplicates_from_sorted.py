def remove_duplicates_from_sorted(arr):
    res=1
    for i in range(1,len(arr)):
        if(arr[i]!=arr[res-1]):
            arr[res] = arr[i]
            res+=1
    return res
arr = [ int(x) for x in input().strip().split()]
temp=remove_duplicates_from_sorted(arr)
for i in range(temp):
    print(arr[i],end=" ")
