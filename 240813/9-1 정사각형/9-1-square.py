cnt=9
n=int(input())
for i in range(n):
    for j in range(n):
        print(cnt,end="")
        cnt-=1
        if cnt<1:
            cnt=9
    print()