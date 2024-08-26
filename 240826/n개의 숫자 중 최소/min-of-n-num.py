k=int(input())
arr=(list(map(int,input().split())))
minv=arr[0]
cnt=0
for elem in arr:
    if elem<minv:
        minv=elem
        cnt=1
    elif minv==elem:
        cnt+=1
print(minv,cnt)