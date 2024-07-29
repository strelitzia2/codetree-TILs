k=int(input())
cnt=0
while k<1000:
    if k%2==0:
        k=k*3+1
        cnt+=1
    elif k%2==1:
        k=k*2+2
        cnt+=1
print(cnt)