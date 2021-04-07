hm={}
def count_freq(arr):
    global hm
    count=0;arr.sort();
    for i in arr:
        if(i in hm):
            hm[i]+=1
        else:
            hm[i]=1
    return hm

def query(x):
    if x in hm:
        return hm[x]
    return 0
arr = [int(x) for x in input().strip().split()]
hm=count_freq(arr)
print(hm)
