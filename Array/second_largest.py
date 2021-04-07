def second_largest(arr):
    largest=0;res=-1
    for i in range(len(arr)):
        if(arr[i]>arr[largest]):
            res=largest
            largest=i
        elif(arr[i] != arr[largest]):
            if(res==-1 or arr[i]>arr[res]):
                res=i
    return res

arr = [ int(x) for x in input().strip().split()]
temp=second_largest(arr)
if(temp == -1):
    print("Not Available")
else:
    print(arr[temp])
    
