def longest_subarray_even_odd(arr,n):
    res=1;curr=1
    for i in range(1,n):
        if((arr[i]%2==0 and arr[i-1]%2!=0) or (arr[i]%2!=0 and arr[i-1]%2==0)):
            curr+=1
            res=max(curr,res)
        else:
            curr=1
    return res

def longestsubarrayevenodd(arr,n):
    res=1
    for i in range(0,n):
        curr=1
        for j in range(i+1,n):
            if((arr[j]%2==0 and arr[j-1]%2!=0) or (arr[j]%2!=0 and arr[j-1]%2==0)):
                curr+=1
            else:
                break
        res=max(curr,res)
    return res

n=int(input())
arr=[int(x) for x in input().strip().split()]
print(str(longest_subarray_even_odd(arr,n))+" "+str(longestsubarrayevenodd(arr,n)))                 
