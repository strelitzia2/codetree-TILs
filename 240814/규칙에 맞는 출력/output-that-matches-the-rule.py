n=int(input())
for i in range(n-1,-1,-1):
    for j in range(1,n+1):
        if i<j:
            print(j,end=" ")
    print()