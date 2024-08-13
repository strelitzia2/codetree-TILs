n=input()
arr=n.split()
a=int(arr[0])
b=int(arr[1])
for i in range(1,10):
    for j in range(b,a-1,-1):
        if j%2==0:
            print(f"{j} * {i} = {i*j} ",end="")
            if j!=a:
                print("/",end=" ")
    print()