n=input()
arr=n.split()
k=0
for i in range(len(arr)):
    if int(arr[i])%3==0:
        break
    else:
        k=int(arr[i])
print(k)