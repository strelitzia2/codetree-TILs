n=int(input())
cnt=1
for i in range(n):
    if i%2==0:
        for j in range(n):
            print(cnt,end=" ")
            cnt+=1
        print()
    else:
        for j in range(n-1,-1,-1):
            print(cnt+j,end=" ")
        cnt+=n
        print()