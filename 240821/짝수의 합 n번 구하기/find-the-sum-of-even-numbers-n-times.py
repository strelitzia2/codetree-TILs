n=int(input())
for i in range(n):
    k=input()
    arr=k.split()
    a=int(arr[0])
    b=int(arr[1])
    s=0
    for j in range(a,b+1):
        if j%2==0:
            s+=j
    print(s)