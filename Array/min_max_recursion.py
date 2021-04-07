def getMin(arr,n):
    if(n==1):
        return arr[0]
    else:
        return min(getMin(arr[1:],n-1),arr[0])
def getMax(arr,n):
    if(n==1):
        return arr[0]
    else:
        return max(getMax(arr[1:],n-1),arr[0])

arr = [ int(x) for x in input().strip().split()]
print(getMin(arr,len(arr)))
print(getMax(arr,len(arr)))
