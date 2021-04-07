def checking_element(arr,x,k):
    temp=[];flag=0;j=0;k1=k
    print(arr)
    for i in range(len(arr)-1):
        if(k>=len(arr)):
            k=len(arr)
        temp = arr[j:k]
        if(x not  in temp):
            flag=1
            return 0
        if(k==len(arr)):
            break
        j=k
        k+=k1
    return 1
arr=[ int(x) for x in input().strip().split()]
x,k = [ int(i) for i in  input().strip().split()]
demo = checking_element(arr,x,k)
if(demo == 1 ):
    print("yes")
else:
    print("no")    
