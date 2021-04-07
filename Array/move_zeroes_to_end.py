def move_zeroes_to_end(arr):
    i=0;j=len(arr)-1
    while(True):
        while(arr[i]!=0 and i<len(arr)):
            i+=1
        while(arr[j]==0 and j>=0):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
arr = [ int(x) for x in input().strip().split()]
move_zeroes_to_end(arr)
print(arr)
                        
