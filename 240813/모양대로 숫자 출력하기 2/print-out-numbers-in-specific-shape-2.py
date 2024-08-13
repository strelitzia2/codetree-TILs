cnt=2
n=int(input())
for i in range(n):
    for j in range(n):
        print(cnt,end=" ")
        cnt+=2
        if cnt>8:
            cnt=2
    print()