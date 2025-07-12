n,d=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
print(sum(arr[-d:]))
