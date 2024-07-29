arr=[]
sum=0
for i in range(5):
    k=int(input())
    arr.append(k)
for i in range(5):
    if arr[i]%3==0:
        sum+=1
if sum==5:
    print(1)
else:
    print(0)