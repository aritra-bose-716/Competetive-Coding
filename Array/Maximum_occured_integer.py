from collections import Counter
def max_Occured(L,R,N,maxx):
    temp=[];hm={}
    for i in range(N):
        x=L[i]
        ran=[]
        while(x<=R[i]):
            ran.append(x)
            x+=1
        temp.append(ran)
    dict1={}
    for i in range(len(temp)):
        coun=Counter(temp[i])
        dict1.add(coun)
    print(dict1)     
    
    
L=[2,1,3];R=[5,3,9]
max_Occured(L,R,len(L),max(R))
