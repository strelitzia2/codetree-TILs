arr=(list(map(int,input().split())))
minv=arr[0]
for elem in arr:
    if elem<minv:
        minv=elem
print(minv)