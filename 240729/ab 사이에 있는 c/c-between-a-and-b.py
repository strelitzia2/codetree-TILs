k=input()
arr=k.split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])
m=b//c+1
good=False
for i in range(1,m+1):

    if c*i>=a and c*i<=b:
        good=True
if good==True:
    print("YES")
else:
    print("NO")