k=input()
arr=k.split()
a=int(arr[0])
b=int(arr[1])
c=False
for i in range(1,a):
    if a%i==0 and b%i==0:
        c=True
        break
if c==True:
    print(1)
else:
    print(0)