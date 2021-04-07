def reverse(arr,n):
    start=0;end=n-1
    while(start<=end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def reverse_alter(arr,n):
    return arr[::-1]
def reverse_recursive(arr,start,end):

    if(start>=end):
        return
    arr[start],arr[end]=arr[end],arr[start]
    return reverse_recursive(arr,start+1,end-1)

arr = [int(x) for x in input().strip().split()]
#reverse(arr,len(arr))
reverse_recursive(arr,0,len(arr)-1)
print(arr)
