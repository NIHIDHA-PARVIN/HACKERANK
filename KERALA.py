n=int(input())
x=[]
for i in range(n):
    arr=list(map(int,input().split()))
    x.append(arr)

count=1
for i in range(n-1):
    if abs(x[i][0]-x[i+1][0])<=abs(x[i][1]-x[i+1][1]):
        continue
    else:
        count+=1
print(count)
