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

def range_coefficient(arr,n):
    min=getMin(arr,n)
    max=getMax(arr,n)
    print(max-min)
    print(round(((max-min)/(max+min)),6))

arr=[ int(x) for x in input().strip().split()]
range_coefficient(arr,len(arr))
