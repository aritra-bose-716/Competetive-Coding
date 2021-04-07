def check_sorted_Array(arr):
    for i in range(1,len(arr)-1):
        if(arr[i]<arr[i-1]):
            return False
    return True
arr = [ int(x) for x in input().strip().split()]
temp=check_sorted_Array(arr)
if(temp == True):
    print("Yes")
else:
    print("No")
                    
