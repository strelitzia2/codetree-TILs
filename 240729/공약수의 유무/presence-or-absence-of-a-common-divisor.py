k=input()
arr=k.split()
a=int(arr[0])
b=int(arr[1])
c=False
for i in range(a,b+1):
    if 1920%i==0 and 2880%i==0:
        c=True
        break
if c==True:
    print(1)
else:
    print(0)