k=input()
arr=k.split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])
con=False
for i in range(a,b+1):
    if c%i==0:
        con=True
        break
if con==False:
    print("NO")
else:
    print("YES")