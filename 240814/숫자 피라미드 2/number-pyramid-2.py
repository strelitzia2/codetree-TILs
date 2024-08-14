cnt=1
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(cnt,end=" ")
        cnt+=1
    print()