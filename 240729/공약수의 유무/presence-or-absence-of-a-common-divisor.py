k=input()
arr=k.split()
a=int(arr[0])
b=int(arr[1])
c=False
for i in range(2,a):
    if a%i==0 and b%i==0:
        c=True
        break
if c==True:
    print(1)
elif c==False:
    print(0)