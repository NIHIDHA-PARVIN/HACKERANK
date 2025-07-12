n=int(input())
stk=[]
reg=0
arr=[]

for i in range(n):
    x=list(input().split())
    arr.append(x)
i=0
while i<n:
    if arr[i][0]=="PUSH":
        stk.append(int(arr[i][1]))
        i+=1
    elif arr[i][0]=="STORE":
        reg=int(stk.pop())
        i+=1
    elif arr[i][0]=="LOAD":
        stk.append(reg)
        i+=1
    elif arr[i][0]=="PLUS":
        frst=stk.pop()
        scnd=stk.pop()
        stk.append(frst+scnd)
        i+=1
    elif arr[i][0]=="TIMES":
        frst=stk.pop()
        scnd=stk.pop()
        stk.append(frst*scnd)
        i+=1 
    elif arr[i][0]=="IFZERO":
        check=stk.pop()
        if check==0:
            i=int(arr[i][1])
        else:
            i+=1
    else:
        print(stk.pop())
        break
        
