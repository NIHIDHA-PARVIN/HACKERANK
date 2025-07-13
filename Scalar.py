n= int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x.sort()
y.sort(reverse=True)
res=0
for i in range(n):
    res+=x[i]*y[i]
print(res)
